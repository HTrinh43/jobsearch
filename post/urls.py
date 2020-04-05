
from . import views
from django.urls import path

urlpatterns = [
	path ('', views.home, name = 'home'),
	path ('newpost/', views.create, name = 'create'),
	path('post/<int:post_id>', views.detail, name = 'detail'),
	path('post/user', views.user_detail, name = 'user_detail'),
	path('post/<int:post_id>/delete', views.delete_post, name = 'delete_post'),
	path('post/<int:post_id>/edit', views.edit_post, name = 'edit_post'),
]