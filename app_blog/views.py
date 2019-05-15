from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
def home(request):
    context={'posts':Post.objects.all()}
    template='app_blog/home.html'
    return render(request,template,context)

def about(request):
    template='app_blog/about.html'
    context={'title':'about'}
    return render(request,template,context)

class PostListView(ListView):
    model=Post
    template='app_blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model=Post
    template='app_blog/blog_detail.html'
    context_object_name='post'
    