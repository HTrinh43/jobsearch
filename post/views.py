from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from account.forms import CreateNewPost
from django.contrib import messages
from django.forms import ModelForm, Form
from django.core.paginator import Paginator


def home(request):
	paginator = Paginator(Post.objects.all(), 10)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1
	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(1)
	# Get the index of the current page
	index = posts.number - 1  # edited to something easier without index
	# This value is maximum index of your pages, so the last page - 1
	max_index = len(paginator.page_range)
	# You want a range of 7, so lets calculate where to slice the list
	start_index = index - 3 if index >= 3 else 0
	end_index = index + 3 if index <= max_index - 3 else max_index
	# Get our new page range. In the latest versions of Django page_range returns
	# an iterator. Thus pass it to list, to make our slice possible again.
	page_range = list(paginator.page_range)[start_index:end_index]
	return render(request, 'main/home.html', {
		'posts': posts,
		'page_range': page_range,})

@login_required
def create(request):
	post=Post()
	if request.method == "POST":
		form=CreateNewPost(request.POST)
		if form.is_valid():
			post.job=form.cleaned_data['job']
			post.workplace=form.cleaned_data['workplace']
			post.address=form.cleaned_data['address']
			post.salary=int(form.cleaned_data['salary'])
			post.description=form.cleaned_data['description']
			post.pub_date=timezone.datetime.now()
			post.author=request.user
			post.worktime=form.cleaned_data['worktime']
			post.save()
			# form.save()

			return redirect('/post/' + str(post.id))
	else:
		form=CreateNewPost()
	return render(request, 'post/create.html', {'form': form})

def detail(request, post_id):
	post=get_object_or_404(Post, pk=post_id)
	return render(request, 'post/detail.html', {'post': post})

def user_detail(request):
	return render(request, 'post/user_detail_posts.html', {'posts': Post.objects.all()})

def delete_post(request, post_id):
	post=get_object_or_404(Post, pk=post_id)
	if request.method == 'POST':
			post.delete()
			messages.success(request, 'Your post has been deleted')
	return render(request, 'main/home.html')


def edit_post(request, post_id):
	post=get_object_or_404(Post, pk=post_id)
	if request.method == 'POST':
		form=CreateNewPost(request.POST, instance=post)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your post has been updated')
			return redirect('/post/' + str(post.id))
		else:
			form=CreateNewPost(instance=post)
	return render(request, 'post/create.html', {'form': form})

def detail_ajax(request, post_id):
	post=get_object_or_404(Post, pk=post_id)
	return render(request, 'post/quickviewJob.html', {'post': post})

