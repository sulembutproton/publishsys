
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views

app_name = 'posts'

urlpatterns = [
    path('list/', views.p_list, name = 'list'),
    path('create/', views.p_create, name = 'create'),
    path('<int:post_id>/delete/', views.p_delete, name = 'delete'),
    path('<int:post_id>/edit/', views.p_edit, name = 'edit'),
    path('<int:post_id>/detail/', views.p_detail, name = 'detail')
]
