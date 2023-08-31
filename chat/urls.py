from django.urls import path

from . import views
urlpatterns = [
    path('create-room/<str:uuid>/',views.create_room,name='create-room'),
]