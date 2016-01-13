import datetime

from django.core.validators import ValidationError
from django.utils.functional import cached_property

from rest_framework import serializers

from .models import Reservation, Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'number', 'capacity', 'price_for_night',)


class ReservationSerializerCreate(serializers.ModelSerializer):
    capacity = serializers.IntegerField()

    class Meta:
        model = Reservation
        fields = ('id', 'user_pk', 'room', 'start_date', 'end_date', 'is_active', 'capacity')
        read_only_fields = ('room',)


    @cached_property
    def _readable_fields(self):
        return [
            field for field in self.fields.values()
            if not field.write_only and not field.field_name == 'capacity'
        ]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.update({'capacity': instance.room.capacity})
        return ret

    def _dates_are_valid(self, start_date, end_date):
        now = datetime.datetime.now().date()
        delta = end_date - start_date
        if delta.days < 1 or start_date < now or end_date < now:
            raise ValidationError('Incorrect dates')
        return True

    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        capacity = data.get('capacity')

        if not self._dates_are_valid(start_date, end_date):
            raise ValidationError('Incorrect dates')

        self.room = Reservation.objects.find_room(start_date, end_date, capacity, exclude=self.instance)

        if not self.room:
            raise ValidationError('No rooms available')

        return data

    def create(self, validated_data):
        validated_data.pop('capacity')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('capacity')
        return super().update(instance, validated_data)

    def save(self, **kwargs):
        return super().save(room=self.room)


class ReservationSerializer(ReservationSerializerCreate):
    room = RoomSerializer()

    class Meta:
        model = Reservation
        fields = ('id', 'user_pk', 'room', 'start_date', 'end_date', 'is_active')


