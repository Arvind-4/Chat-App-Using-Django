from django.urls import path
from .views import home, room, checkview, send, getMessages

urlpatterns = [
    path("", home, name="Home"),
    path("<str:room>/", room, name="room"),
    path("checkview", checkview, name="checkview"),
    path("send", send, name="send"),
    path("getMessages/<str:room>/", getMessages, name="getMessages"),
]
