from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('categories/', views.getCategories),
    path('categoryProvider/<str:pk>/', views.getCategorieProvider),
    path('providers/', views.getProviders),
    path('providers/<str:pk>/', views.getProvider),
    path('users/', views.getUsers),
    path('users/<str:pk>/', views.getUser),

    re_path('login', views.login),
    re_path('signup', views.signUp),
    re_path('testtoken', views.testToken),
   
]