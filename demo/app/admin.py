from django.contrib import admin
from . models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    list_display = ['first_name', 'last_name', 'number', 'date' ]

admin.site.register(Feedback, FeedbackAdmin)