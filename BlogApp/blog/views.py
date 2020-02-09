from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.



#define your name => context_object_name = ''
#default name =>object_list
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

#default name=>object
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

