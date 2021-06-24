from django.contrib import admin
from courses.models import Question, Choice,Course


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    filter_horizontal = ('choice',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Course)

