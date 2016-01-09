from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


from .models import Room, Reservation
from .serializers import RoomSerializer, ReservationSerializer
from core.utlis import JSONResponse


@csrf_exempt
def room_list(request):
    rooms = Room.objects.all()
    room_serializer = RoomSerializer(rooms, many=True)
    return JSONResponse(room_serializer.data)


@csrf_exempt
def reservation_list(request):
    if request.method == 'GET':
        reservations = Reservation.objects.all()
        reservation_serializer = ReservationSerializer(reservations, many=True)
        return JSONResponse(reservation_serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        reservation_serializer = ReservationSerializer(data=data)
        if reservation_serializer.is_valid():
            reservation_serializer.save()
            return JSONResponse(reservation_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(reservation_serializer.data, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def reservation_active_list(request):
    reservations = Reservation.objects.active()
    reservation_serializer = ReservationSerializer(reservations, many=True)
    return JSONResponse(reservation_serializer.data)


@csrf_exempt
def reservation_inactive_list(request):
    reservations = Reservation.objects.inactive()
    reservation_serializer = ReservationSerializer(reservations, many=True)
    return JSONResponse(reservation_serializer.data)


@csrf_exempt
def user_reservation_list_active(request, user_pk):
    if not get_user_model().objects.filter(pk=user_pk).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    reservations = Reservation.objects.user_active(user_pk)
    reservation_serializer = ReservationSerializer(reservations, many=True)
    return JSONResponse(reservation_serializer.data)


@csrf_exempt
def user_reservation_list_inactive(request, user_pk):
    if not get_user_model().objects.filter(pk=user_pk).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    reservations = Reservation.objects.user_inactive(user_pk)
    resevation_serializer = ReservationSerializer(reservations, many=True)
    return JSONResponse(resevation_serializer.data)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer