from django.urls import path, include
from booking import views
from booking.views import home, relax, kitchen, room, post_booking


urlpatterns = [

    path('', home, name="home"),
    path('booking/<slug:slug>/', views.RoomTypeBookingView.as_view(), name='booking'),
    path('room/', room, name="room"),
    path('kitchen/', kitchen, name="kitchen"),
    path('relax/', relax, name="relax"),
    path('dashboard/', include('dashboard.urls')),
    path('room_type/<slug:slug>/', views.RoomTypeView.as_view(), name='room-name'),
    path('post_booking/', post_booking, name="post-booking"),

    # path('date/', views.post_order_waiting, name="post_order_waiting"),

    # path('order/', views.OrderList.as_view()),
    # path('room/', views.RoomList.as_view()),
    # path('roomtype/', views.RoomTypeList.as_view()),
    # path('order1/', views.Order1List.as_view()),
    # path('room1/', views.Room1List.as_view()),
    # path('roomtype1/', views.RoomType1List.as_view()),
    # path('date/', views.RoomType1List.as_view()),
    # path('room_type/<slug:slug>/', views.RoomTypeView.as_view(), name='room-name')
]