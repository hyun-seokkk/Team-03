from django.urls import path
from . import views

app_name = 'dinings'
urlpatterns = [
    path('', views.index, name='index'),
    path('showmap/', views.showmap, name='showmap'),
    path('create/', views.dining_create, name='dining_create'),
    path('update/<int:dining_pk>', views.dining_update, name='dining_update'),
    path('delete/<int:dining_pk>', views.dining_delete, name='dining_delete'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:dining_pk>/reviews/', views.review_create, name='review_create'),
    path('<int:dining_pk>/reviews/<int:review_pk>/',
         views.review_detail, name='review_detail'),
    path('<int:dining_pk>/reviews/<int:review_pk>/update/',
         views.review_update, name='review_update'),
    path('search/', views.search, name='search'),
    path('<int:dining_pk>/menus', views.menu_create, name='menu_create'),
    path('<int:dining_pk>/likes/', views.likes, name='likes'),
    path('<int:dining_pk>/reviews/<int:review_pk>/delete/', views.review_delete, name='review_delete'),
    path('<int:dining_pk>/reviews/<int:review_pk>/like/', views.review_like, name='review_like'),
    path('<int:dining_pk>/menus/<int:menu_pk>/delete/', views.menu_delete, name='menu_delete'),

]
