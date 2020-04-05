from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import RegisterForm
from django import forms

def signup(request):
	# Create your views here.

	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			user = authenticate(request,username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
			auth.login(request, user)
			return redirect("/")
	else:
		form = RegisterForm()

	return render(request, "registration/signup.html", {"form":form})

