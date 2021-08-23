from django.contrib import admin
from .models import Room, RoomType, Order, Menu, Items, Room_info, Room_photo, Order_waiting


class Rommetype(admin.ModelAdmin):
    list_display = ['type', 'slug']


admin.site.register(Room)
admin.site.register(RoomType, Rommetype)
admin.site.register(Order)
admin.site.register(Menu)
admin.site.register(Items)
admin.site.register(Room_info)
admin.site.register(Room_photo)
admin.site.register(Order_waiting)
