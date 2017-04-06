from django import forms

class QuestionForm(forms.Form):
    answer = forms.FloatField(label=None)
