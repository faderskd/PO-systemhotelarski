import datetime

from django.core.validators import ValidationError

from rest_framework import serializers

from .models import Reservation, Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'number', 'capacity', 'price_for_night',)


class ReservationSerializerCreate(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = ('id', 'user_pk', 'start_date', 'end_date', 'is_active')

    def get_is_active(self, obj):
        return obj.is_active

    def _dates_are_valid(self, start_date, end_date):
        now = datetime.datetime.now().date()
        delta = end_date - start_date
        if delta.days < 1 or start_date < now or end_date < now:
            raise ValidationError('Incorrect dates')
        return True

    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if not self._dates_are_valid(start_date, end_date):
            raise ValidationError('Incorrect dates')

        room = self.instance.room if self.instance else None
        self.room = Reservation.objects.find_room(start_date, end_date, exclude=room)

        if not self.room:
            raise ValidationError('No rooms available')

        return data

    def save(self, **kwargs):
        return super().save(room=self.room)

class ReservationSerializer(ReservationSerializerCreate):
    room = RoomSerializer()

    class Meta:
        model = Reservation
        fields = ('id', 'user_pk', 'room', 'start_date', 'end_date', 'is_active')


