from django.urls import path
from . import views as posts_views

urlpatterns =[
    path('<str:slug>',posts_views.post,name="post"),
    path('',posts_views.index,name="posts")
]