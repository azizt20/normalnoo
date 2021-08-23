from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from .models import RoomType, Room, Order, Menu, Room_info, Room_photo, Items, Order_waiting
from rest_framework import generics
from rest_framework.response import Response
from .serializers import DateModelSerializer, RoomTypeModelSerializer, RoomModelSerializer, OrderModelSerializer, \
    Order1ModelSerializer, Room1ModelSerializer, RoomType1ModelSerializer
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

# Create your views here.

date_now = (datetime.datetime.now() - datetime.timedelta(days=10))
qwerty = []
for i in range(30):
    qwerty.append((date_now + datetime.timedelta(days=i)).date())



class RoomTypeList(generics.ListCreateAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeModelSerializer


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer


class RoomType1List(generics.ListCreateAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomType1ModelSerializer


class Room1List(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = Room1ModelSerializer


class Order1List(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = Order1ModelSerializer




def home(request):
    request.session['st_d'] = ''
    request.session['en_d'] = ''
    request.session['d'] = ''
    room_all = RoomType.objects.all()
    return render(request, 'home.html', {'r_all': room_all})


def room(request):
    return render(request, 'room.html')


# def booking(request):
#     return render(request, 'booking.html')

def relax(request):
    room_all = RoomType.objects.all()
    return render(request, 'relax.html', {'r_all': room_all})


def kitchen(request):
    menu = Menu.objects.all()
    room_all = RoomType.objects.all()
    return render(request, 'kitchen.html', {'m': menu, 'r_all': room_all})


def room(request):
    room_info = Room_info.objects.all()
    return render(request, 'room.html', {'r_i': room_info})



class RoomTypeView(View):
    def get(self, request, slug):
        room = RoomType.objects.get(slug=slug)


        room_all = RoomType.objects.all()
        datafaziz = {'room': room, 'r_all': room_all}

        countORooms = Room.objects.filter(room_type=room)
        xonalar = Order.objects.filter(room__room_type=room)
        busydays = []
        for x in xonalar:
            sd = x.start_date
            fd = x.finish_date
            day = fd - sd

            for single_date in (sd + datetime.timedelta(n) for n in range(int(day.days))):
                busydays.append(single_date)
        sott = sorted(busydays)
        listbme = []
        finishlist = []
        count = 1
        for inum in sott:

            if inum in listbme:
                count += 1
                print(inum)
            listbme.append(inum)
            if count == len(countORooms):
                finishlist.append(inum)
                count = 1
        print('----------------')
        print(finishlist)
        print('----------------')
        datafaziz['busy'] = finishlist


        print(datafaziz)
        return render(request, 'room_type.html', datafaziz)


class RoomTypeBookingView(View):
    def get(self, request, slug):
        room = RoomType.objects.get(slug=slug)
        room_all = RoomType.objects.all()
        request.session['type'] = room.type
        return render(request, 'booking.html', {'room': room, 'r_all': room_all})

    def get(self, request, slug):
        room = RoomType.objects.get(slug=slug)


        room_all = RoomType.objects.all()
        datafaziz = {'room': room, 'r_all': room_all}

        countORooms = Room.objects.filter(room_type=room)
        xonalar = Order.objects.filter(room__room_type=room)
        busydays = []
        for x in xonalar:
            sd = x.start_date
            fd = x.finish_date
            day = fd - sd

            for single_date in (sd + datetime.timedelta(n) for n in range(int(day.days))):
                busydays.append(single_date)
        sott = sorted(busydays)
        listbme = []
        finishlist = []
        count = 1
        for inum in sott:

            if inum in listbme:
                count += 1
                print(inum)
            listbme.append(inum)
            if count == len(countORooms):
                finishlist.append(inum)
                count = 1
        print('----------------')
        print(finishlist)
        print('----------------')
        datafaziz['busy'] = finishlist


        print(datafaziz)
        return render(request, 'booking.html', datafaziz)



def post_booking(request):

    if request.method == 'POST':
        room = request.POST.get('room')
        start_date = request.POST.get('start_date')
        finish_date = request.POST.get('finish_date')

        order_cost = request.POST.get('order_cost')
        user_name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        pay = request.POST.get('pay')
        valid_phone = None
        if phone_number.startswith('+') and phone_number[1:].isdigit():
            valid_phone = phone_number
        else:
            messages.warning(request, 'введите номер в правельном формате ')
            request.session['st_d']=request.POST.get("start_date")
            request.session['en_d']=request.POST.get("finish_date")
            request.session['d']=request.POST.get("days")
            return redirect('booking', request.GET.get('slug'))

        wait = Order_waiting()
        wait.room = room
        wait.start_date = str(start_date)
        wait.finish_date = str(finish_date)
        wait.order_cost = order_cost
        wait.user_name = user_name
        wait.phone_number = valid_phone
        wait.email = email
        wait.pay = pay
        wait.save()
        return redirect('home')
    return render(request, 'booking.html')
