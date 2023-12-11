from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import Room, Messages

# Create your views here.


def home(request):
    return render(request, "home.html", context={})


def room(request, room):
    username = request.GET.get("username")
    room_details = Room.objects.get(name=room)
    context = {"username": username, "room": room, "room_details": room_details}
    return render(request, "room.html", context=context)


def checkview(request):
    room = request.POST["room_name"]
    username = request.POST["username"]

    if Room.objects.filter(name=room).exists():
        return redirect(f"/{room}/?username={username}")

    else:
        new_room = Room.objects.create(name=room)
        new_room.save()

        return redirect(f"/{room}/?username={username}")


def send(request):
    username = request.POST["username"]
    room_id = request.POST["room_id"]
    message = request.POST["message"]

    new_message = Messages.objects.create(user=username, room=room_id, value=message)
    new_message.save()
    return HttpResponse("Message Sent Successfully")


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    message = Messages.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(message.values())})
