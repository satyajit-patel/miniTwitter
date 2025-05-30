from django.urls import path
from .import views

urlpatterns = [
    path('', views.tweetList, name='tweetList'),
    path('create/', views.tweetCreate, name='tweetCreate'),
    path('<int:tweetId>/edit/', views.tweetEdit, name='tweetEdit'),
    path('<int:tweetId>/delete/', views.tweetDelete, name='tweetDelete'),
    path('register/', views.register, name='register'),
]
