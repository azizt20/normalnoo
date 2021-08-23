from django import template
from booking.models import RoomType
from booking.models import Room
from booking.models import Order

register = template.Library()


@register.filter(name='filter_me')
def filter_me(data):
    # print(data)
    orders = Order.objects.all()
    diff_day = ''
    user_name = ''
    for i in orders:
        if data == i.start_date:
            myOrder = i
            diff_day = str(myOrder.diff_days)
            user_name = str(myOrder.user_name)
    print(diff_day)
    text = f"<th scope='col' colspan=' {diff_day} ' class='ordered'> {user_name} </th>"
    return text


@register.simple_tag()
def build_key(room, day):
    return "{}_{:%Y-%m-%d}".format(room.id, day)


@register.simple_tag()
def get_item(dictionary, key):
    return dictionary.get(key)
