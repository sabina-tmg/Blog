from django.urls import path
from.views import *

urlpatterns=[
    path("",home,name="home"),
     path('blog/',blog, name='blog'),
    path('postcomment/',PostComment, name="postcomment"),

    path('blogpost/<str:slug>',blogpost, name='blogpost'),
    path('search/',search, name='search'),
    path('contact/',contact, name='contact'),
    path('home/',main, name="Ghar"),
]