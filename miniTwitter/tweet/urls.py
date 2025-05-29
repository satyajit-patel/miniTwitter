from django.urls import path
from .import views

urlpatterns = [
    path('create/', views.tweetList, name='tweetCreate'),
    path('<int:tweetId>/edit/', views.tweetCreate, name='tweetEdit'),
    path('<int:tweetId>/delete/', views.tweetDelete, name='tweetDelete'),
]
