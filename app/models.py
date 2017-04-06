from django.db import models

from django.conf import settings
from .helpers import Anchoring
from common.utils import ChoiceEnum
from ckeditor.fields import RichTextField


class QuestionStageTypes(ChoiceEnum):
    plain_number = 0
    random_fact = 1
    targeted_fact_far_off = 2
    targeted_fact_close = 3


class Question(models.Model):
    description = models.CharField(max_length=100, null=True)
    answer = models.IntegerField(default=0)
    source = models.TextField(max_length=1000, null=True)
    def __str__(self):
        return self.description


class QuestionBiasGenerator(models.Model):
    type = models.CharField(max_length=1, choices=QuestionStageTypes.choices())
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=100)
    is_higher = models.BooleanField(default=True)


class UserAnswersQuestion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    bias_question = models.ForeignKey(QuestionBiasGenerator, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now=True)
    is_answered = models.BooleanField(default=False)
    answer = models.FloatField(default=None, null=True)

    def save(self, *args, **kwargs):
        self.add_bias_question()
        super(UserAnswersQuestion, self).save(*args, **kwargs)

    def get_anchoring(self):
        cnt = UserAnswersQuestion.objects.filter(user=self.user.id).exclude(is_answered=False).count()
        return Anchoring(self.user, cnt)

    def add_bias_question(self):
        a = self.get_anchoring()
        stage = a.get_user_stage()
        type_list = []
        if stage is 0 or stage is 1:
            type_list = [QuestionStageTypes.plain_number.value, QuestionStageTypes.random_fact.value]
        if stage is 2 or stage is 3:
            type_list = [QuestionStageTypes.targeted_fact_far_off.value, QuestionStageTypes.targeted_fact_close.value]

        self.bias_question = QuestionBiasGenerator.objects.filter(question=self.question).filter(type__in=type_list)[0]


class ExplanationTexts(models.Model):
    location = models.CharField(max_length=20, null=True)
    text = RichTextField()

    def __str__(self):
        return self.location;