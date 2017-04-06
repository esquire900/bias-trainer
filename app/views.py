from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from lazysignup.decorators import allow_lazy_user
from .models import Question, UserAnswersQuestion, ExplanationTexts
from .forms import QuestionForm


@allow_lazy_user
def new_question(request):
    answered_ids = UserAnswersQuestion.objects.filter(user=request.user.id).exclude(is_answered=False).values(
        'question').distinct()
    try:
        q = Question.objects.exclude(id__in=answered_ids)[0]
    except IndexError:
        return HttpResponse("Hmm seems we've ran out of questions for you!")
    user_answers_question = UserAnswersQuestion(user=request.user, question_id=q.id)
    user_answers_question.save()
    return HttpResponseRedirect('/question/{}'.format(user_answers_question.id))


@allow_lazy_user
def question(request, question_id):
    user_answers_question = UserAnswersQuestion.objects.get(pk=question_id)
    if user_answers_question.is_answered:
        return HttpResponseBadRequest("You've already answered this one!")

    display_location = user_answers_question.get_anchoring().get_display_explanation()
    if display_location is not False:
        content = ExplanationTexts.objects.get(location=display_location)
        content = content.text
    else:
        content = False

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            user_answers_question.is_answered = True
            user_answers_question.user_answer = form.cleaned_data['answer']
            user_answers_question.save()
            return HttpResponseRedirect('/question/new')
    else:
        form = QuestionForm()
    context = {'form': form, 'question': user_answers_question.question,
               'bias_question': user_answers_question.bias_question, 'id': question_id, 'content': content,
               'has_content': content is not False}

    return render(request, 'app/question.html', context)


@allow_lazy_user
def home(request):
    content = ExplanationTexts.objects.get(location='home')
    context = {'user': request.user, 'content': content.text}
    return render(request, 'app/home.html', context)


@allow_lazy_user
def anchor(request):
    context = {'user': request.user}
    return render(request, 'app/anchor.html', context)
