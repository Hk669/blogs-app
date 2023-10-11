from django.contrib import admin
from django.urls import path
from blogs import views

urlpatterns = [
    path('',views.home, name='blog-home'),
    # path('about/', views.about, name='blog-about'),
    path('blogpost/', views.create_blog, name='create_blog'),
    path('delete/<int:pk>/',views.delete_blog, name="delete_blog"),
    path('blog/<int:pk>/',views.blog_post_detail, name="blog_post_detail"),
]
