import datetime

from django.db import models
from django.urls import reverse_lazy


# Create your models here.
class RoomType(models.Model):
    type = models.CharField(max_length=50, blank=True)
    min_cost = models.FloatField()
    title = models.CharField(max_length=200, null=True, blank=True)
    info = models.CharField(max_length=200, null=True, blank=True)
    photo1 = models.ImageField(upload_to='avatars/', null=True, blank=True)
    photo2 = models.ImageField(upload_to='avatars/', null=True, blank=True)
    photo3 = models.ImageField(upload_to='avatars/', null=True, blank=True)
    cost_day = models.IntegerField(null=True, blank=True)
    is_villa = models.BooleanField(default=False)

    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse_lazy('room-name', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.type}'


class Room_info(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    info = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.room_type}'


class Room_photo(models.Model):
    room_info = models.ForeignKey(Room_info, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f'{self.id}'


class Room(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.IntegerField()
    slug = models.SlugField()
    description = models.CharField(max_length=200)
    bed_count = models.IntegerField()
    capacity = models.IntegerField()
    cost_per_day = models.IntegerField()

    def get_absolute_url(self):
        return f'/{self.room_type.slug}/{self.slug}'

    def __str__(self):
        return f'{self.room_type} {self.room_number} '


class Order(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='orders')
    slug = models.SlugField()
    start_date = models.DateField()
    finish_date = models.DateField()
    order_cost = models.IntegerField()
    user_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    @property
    def diff_days(self):
        return int((self.finish_date - self.start_date).days)

    def get_absolute_url(self):
        return f'/{self.room.room_type.slug}/{self.room.slug}/{self.slug}'

    def __str__(self):
        return f'{self.id} '


class Order_waiting(models.Model):
    room = models.CharField(max_length=200, blank=True)
    start_date = models.CharField(max_length=200, blank=True)
    finish_date = models.CharField(max_length=200, blank=True)
    order_cost = models.IntegerField(null=True, blank=True)
    pay = models.CharField(max_length=200, blank=True)
    user_name = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=14, blank=True)
    email = models.CharField(max_length=200, blank=True, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.user_name}'


class Menu(models.Model):
    type = models.CharField(max_length=225, blank=True)

    def __str__(self):
        return f'{self.type}'


class Items(models.Model):
    type_menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    dish = models.CharField(max_length=225)
    cost = models.IntegerField()

    def __str__(self):
        return f'{self.dish}'
