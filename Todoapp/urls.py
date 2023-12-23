from django.urls import path
from . import views
from .views import delete_todo, finish_todo

urlpatterns = [
    path('', views.index, name='index') ,
    path('todo/', views.create_todo, name='create_todo'),
    path('login/',views.loginn,name='login'), 
    path('register/',views.register,name='register'), 
    path('todo/<int:todo_id>/delete/', delete_todo, name='delete_todo'),
    path('todo/<int:todo_id>/finish/', finish_todo, name='finish_todo'),
    path('logout/',views.logout,name='logout'), 
]
