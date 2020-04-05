from django.contrib import admin

from .models import Question, Choice

class ChoiceAdmin(admin.ModelAdmin):
	raw_id_fields = ["question"]

admin.site.register(Choice, ChoiceAdmin)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    date_hierarchy = 'pub_date'

    fieldsets = [
        (None,               {'fields': ['question_text', 'question_text_long']}),
        ('Int information',  {'fields': ['views']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('id', 'question_text', 'pub_date', 'views', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)