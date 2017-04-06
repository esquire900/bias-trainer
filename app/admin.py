from django.contrib import admin
from .models import Question, UserAnswersQuestion, QuestionBiasGenerator, ExplanationTexts

# Register your models here.

class BiasInline(admin.TabularInline):
    model = QuestionBiasGenerator

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        BiasInline,
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(UserAnswersQuestion)
admin.site.register(ExplanationTexts)