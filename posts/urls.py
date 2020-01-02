# posts/urls.py
from django.conf.urls import url
from django.urls import path

from .views import HomePageView

from posts.views import productdetail

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('product/<int:id>', productdetail, name="product")
]