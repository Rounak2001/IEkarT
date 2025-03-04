from django.urls import path
from .views import chat_room

urlpatterns = [
    path('', chat_room, name="chat_room"),
]
