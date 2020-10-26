from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('save/', views.save, name='save'),
    path('<int:task_id>/', views.detail, name='details'),
    path('<int:task_id>/update/', views.update, name='update')
]
