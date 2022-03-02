from django.contrib import admin
from . models import Feedback, Question, Gallery


class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    list_display = ['first_name',  'number', 'date']


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ['question',  'answer']

class GalleryAdmin(admin.ModelAdmin):
    model = Gallery
    list_display = ['id']



admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Question, QuestionAdmin)

admin.site.register(Gallery, GalleryAdmin)