from rest_framework import serializers
from booking.models import RoomType, Room, Order
import datetime



date_now = (datetime.datetime.now() - datetime.timedelta(days=10))
qwerty = []
for i in range(30):
    qwerty.append((date_now + datetime.timedelta(days=i)).date())

class DateModelSerializer(serializers.ModelSerializer):
    date = serializers.DateField()



class RoomTypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'


class RoomModelSerializer(serializers.ModelSerializer):
    # room_type = RoomTypeModelSerializer()

    class Meta:
        model = Room
        fields = '__all__'


class OrderModelSerializer(serializers.ModelSerializer):
    room = RoomModelSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class Order1ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class Room1ModelSerializer(serializers.ModelSerializer):
    orders = Order1ModelSerializer(many=True)

    class Meta:
        model = Room
        fields = '__all__'


class RoomType1ModelSerializer(serializers.ModelSerializer):
    rooms = Room1ModelSerializer(many=True)

    class Meta:
        model = RoomType
        fields = '__all__'
