from . import views
from django.views.generic import RedirectView
from django.urls import path


urlpatterns = [
    # path(r'', RedirectView.as_view(url='home', permanent=False)),
    path('shortstories/', views.ArtsPostList.as_view(), name='shortstories'),
    path('books/', views.BooksPostList.as_view(), name='books'),
    path('films/', views.FilmsPostList.as_view(), name='films'),
    path('travel/', views.TravelPostList.as_view(), name='travel'),
    path('interviews/', views.InterviewsPostList.as_view(), name='interviews'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.PostList.as_view(), name='home'),
]