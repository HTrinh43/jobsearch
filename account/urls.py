from . import views
from django.urls import path
from django.contrib import admin
urlpatterns = [
	path('signup/', views.signup, name = 'signup'),
]