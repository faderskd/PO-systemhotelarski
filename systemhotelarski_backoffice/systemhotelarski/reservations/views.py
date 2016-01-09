from rest_framework import viewsets
from rest_framework.response import Response

from .models import Room, Reservation
from .serializers import RoomSerializer, ReservationSerializer
from core.utlis import JSONResponse


def room_list(request):
    rooms = Room.objects.all()
    room_serializer = RoomSerializer(rooms, many=True)
    return JSONResponse(room_serializer.data)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer