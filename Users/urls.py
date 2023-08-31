from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('register/',views.Register.as_view(),name='register'),
    path('profile/',views.Profile.as_view(),name='user-profile'),
]
