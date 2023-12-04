from django.urls import path
from . import views
from .views import post_list,post_detail,post_new, post_edit

urlpatterns = [
    path('', post_list.as_view(), name='post_list'),
    path('post/<int:pk>/', post_detail.as_view(), name='post_detail'),
    path('post/new', post_new.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', post_edit.as_view(), name='post_edit'),
]