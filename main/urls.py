from django.contrib import admin
from django.urls import path, include
from main import views
from .views import home,add_todo,delete_todo
urlpatterns = [
    path('', views.home, name='home'),
    path('add_todo/', views.add_todo),
    path('delete_todo/<int:todo_id>/', views.delete_todo),
    
]
