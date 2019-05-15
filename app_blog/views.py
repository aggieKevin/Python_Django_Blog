from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
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
    template_name='app_blog/home.html' 
    # if note created, the view will use default template
    #<app>/<model>_<viewtype>.html
    context_object_name='posts'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model=Post
    template_name='app_blog/blog_detail.html'
    context_object_name='post'
    
class PostCreateView(LoginRequiredMixin,CreateView): # how to require log in for class view
    model=Post
    fields=['title','content']
    template_name='app_blog/blog_create.html'
    context_object_name='form'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): # how to require log in for class view
    model=Post
    fields=['title','content']
    template_name='app_blog/blog_create.html'
    context_object_name='form'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    context_object_name='post' # the default name is object
    template_name='app_blog/blog_delete.html'
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False