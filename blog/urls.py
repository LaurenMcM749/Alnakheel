from . import views
from django.urls import path

urlpatterns = [
    path('home', views.PostList.as_view(), name='home'),
    path('home/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('home/arts', views.ArtsPostList.as_view(), name='arts'),
    path('home/books', views.BooksPostList.as_view(), name='books'),
    path('home/films', views.FilmsPostList.as_view(), name='films'),
    path('home/travel', views.TravelPostList.as_view(), name='travel'),
    path('home//interviews/', views.InterviewsPostList.as_view(), name='interviews'),
    path('home/about', views.AboutView.as_view(), name='about'),
]