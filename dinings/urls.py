from django.urls import path
from . import views

app_name = 'dinings'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.dining_create, name='dining_create')
]
