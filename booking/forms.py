from django import forms
from .models import Order


class BookingForm(forms.ModelForm):
    class Meta:
        model = Order
        # order_cost = Order.count_day * Order.room.cost_per_day
        exclude = ['order_cost']
        widgets = {
            'start_date': forms.TextInput(attrs={'type': 'date'}),
            'finish_date': forms.DateInput,
        }
