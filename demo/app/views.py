from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from app.models import Feedback, Question, Gallery
from users.forms import CustomUserCreationForm
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from users.forms import CustomUserCreationForm



def index(request):
    gallery = Gallery.objects.order_by('-id')
    return render(request, 'pages/index.html', {'gallery':gallery})


def question(request):
    questions = Question.objects.order_by('-id')
    return render(request, 'pages/question.html', {'questions':questions})


def feedback(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        number = request.POST.get('number')
        text = request.POST.get('text')

        feedback = Feedback()
        feedback.first_name = first_name
        feedback.number = number
        feedback.text = text
        feedback.save()
        return redirect('success')

def success(request):
    return render(request, 'pages/success.html')

def sign_in(request):
    message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
      
        if user is not None :
            login(request, user)
            return redirect('index')
        else:
            message = 'Такого пользователя не существует.'   
            return HttpResponse(message)
           
    else:
        return render(request, 'pages/sign_in.html')


def sign_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')


def sign_up(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  
            user = form.save()
            login(request, user)
            # messages.success(request, 'Account created successfully')
            return redirect('index')
        else:
            messages = ValidationError(list(form.errors.values()))
            return render(request, 'pages/sign_up.html', {'form':form, 'messages':messages})
           
    else:
        form = CustomUserCreationForm()
        return render(request, 'pages/sign_up.html', {'form':form})


