# posts/views.py
from django.views.generic import ListView
from django.shortcuts import render
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'index.html'


def productdetail(request, id):
   product = Post.objects.get(id=id)
   return render(request, 'product.html', {'product': product})