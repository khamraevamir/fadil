from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-out/', views.sign_out, name='sign_out'),
    path('sign-up/', views.sign_up, name='sign_up'),

    path('feedback', views.feedback, name='feedback'),
    path('success', views.success, name='success'),

    path('question/', views.question, name='question'),
]
