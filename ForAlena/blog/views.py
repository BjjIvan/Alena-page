from django.shortcuts import render, redirect
from .forms import SignUpForm, ContactForm
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lecture
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User

def home(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('blog:lectures')
    else:
         form = UserCreationForm()

    return render(request,'blog/sign_up.html',{'form':form})

def lecture(request):
      lecture = Lecture.objects.get(date_start=timezone.now())
      return render(request,'blog/sad2.html', {'lecture':lecture})
