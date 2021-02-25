from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'detail_information'  # added by me, so object has a more specific name
