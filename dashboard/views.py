from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout, get_user_model
import datetime

from .forms import LoginForm
from .models import User_staff
from booking.forms import BookingForm
from booking.models import RoomType, Order_waiting, Room, Order


class Dashboard(View):
    def get(self, request, start=None):
        user = request.user
        print(user)
        datatime_list = []
        asd = datetime.datetime.now() - datetime.timedelta(10)

        start_date = None
        if start is not None:
            start_date = datetime.datetime.strptime(start, "%Y-%m-%d")
            asd = start_date

        for i in range(30):
            datatime_list.append(asd + datetime.timedelta(i))
        data = {}
        skip = set()

        orders = Order.objects.select_related('room')
        if start is not None:
            orders = orders.filter(Q(start_date__gte=start) | Q(finish_date__gte=start))

        for order in orders.all():
            if start is not None:
                if order.start_date < start_date.date():
                    order.start_date = start_date.date()

            key = "{}_{:%Y-%m-%d}".format(order.room_id, order.start_date)
            data[key] = order

            current = (order.start_date + datetime.timedelta(days=1))
            while current <= order.finish_date - datetime.timedelta(days=1):
                key = "{}_{:%Y-%m-%d}".format(order.room_id, current)
                skip.add(key)
                current = (current + datetime.timedelta(days=1))

        context = {
            'form': BookingForm(),
            'current_Date': datetime.date.today(),
            'month': datatime_list,
            'data': data,
            'skip': skip,
            'types': RoomType.objects.all(),
            'rooms': Room.objects.all()
        }
        if user.is_authenticated:
            return render(request, 'dashboard/dashboard.html', context)
        else:
            return redirect("login")

    def post(self, request):
        room = Room.objects.get(slug=request.POST['room'])
        order = Order(
            room=room,
            slug=request.POST['slug'],
            start_date=request.POST['start'],
            finish_date=request.POST['finish'],
            order_cost=request.POST['price'],
            user_name=request.POST['name'],
            phone_number=request.POST['number'],
            email=request.POST['email']
        )
        order.save()

        return redirect('dashboard')


class Edit_order(View):

    def post(self, request):
        room = Room.objects.get(slug=request.POST['room'])
        order = Order.objects.get(id=request.POST['id'])

        order.room = room
        order.slug = request.POST['slug']
        order.start_date = request.POST['start']
        order.finish_date = request.POST['finish']
        order.order_cost = request.POST['price']
        order.user_name = request.POST['name']
        order.phone_number = request.POST['number']
        order.email = request.POST['email']

        order.save()

        return redirect('dashboard')


def order_list(request):
    content = {
        'orders': Order.objects.order_by('created_at')
    }
    return render(request, 'dashboard/list_orders.html', content)


def online_order_list(request):
    if request.method == 'POST':
        name = request.POST['names']
        print('salom')
        content = {
            'orders': Order_waiting.objects.filter(user_name__contains=name),
            'rooms': Room.objects.all()
        }
        return render(request, 'dashboard/list_online_orders.html', content)
    content = {
        'orders': Order_waiting.objects.all().order_by('-created_at'),
        'rooms': Room.objects.all()
    }
    return render(request, 'dashboard/list_online_orders.html', content)


def delete_waiting(request, pk):
    Order_waiting.objects.get(id=pk).delete()
    return redirect('online-order_list')

class UserLoginView(View):
    """ User Login """

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = LoginForm()
        context = {'form': form}
        return render(request, 'auth.html', context)

    def post(self, request):
        form = LoginForm(data=request.POST)
        print('shetdan utmebdi')
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'],
                                backend='django.contrib.auth.backends.ModelBackend')
            print('sihlavottiku')
            if user is not None:
                login(request, user)
                print('sihlavotti')
                return redirect('dashboard')
            else:
                # messages.error(request, 'Username or Password is invalid')
                context = {'form': form}
                return render(request, 'auth.html', context)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

#
# class DashHome(TemplateView):
#     template_name = 'dashboard/dashboard.html'
#
#     def get_context_data(self, **kwargs):
#         start = None
#         context = super(DashHome, self).get_context_data(**kwargs)
#         datatime_list = []
#         asd = datetime.datetime.now() - datetime.timedelta(10)
#         start_date = None
#         if start is not None:
#             start_date = datetime.datetime.strptime(start, "%Y-%m-%d")
#             asd = start_date
#
#         for i in range(30):
#             datatime_list.append(asd + datetime.timedelta(i))
#         data = {}
#         skip = set()
#
#         orders = Order.objects.select_related('room')
#         if start is not None:
#             orders = orders.filter(Q(start_date__gte=start) | Q(finish_date__gte=start))
#
#         for order in orders.all():
#             if start is not None:
#                 if order.start_date < start_date.date():
#                     order.start_date = start_date.date()
#
#             key = "{}_{:%Y-%m-%d}".format(order.room_id, order.start_date)
#             data[key] = order
#
#             current = (order.start_date + datetime.timedelta(days=1))
#             while current <= order.finish_date:
#                 key = "{}_{:%Y-%m-%d}".format(order.room_id, current)
#                 skip.add(key)
#                 current = (current + datetime.timedelta(days=1))
#
#         context = {
#             'form': BookingForm(),
#             'current_Date': datetime.date.today(),
#             'month': datatime_list,
#             'data': data,
#             'skip': skip,
#             'types': RoomType.objects.all(),
#             'rooms': Room.objects.all()
#         }
#
#         return context
