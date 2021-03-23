from django import forms

from ordersapp.models import OrderItem


class OrderItemForm(forms.ModelForm):
    """
    Форма бронирования мест в походе.
    """
    options_used = forms.MultipleChoiceField(required=False)

    class Meta:
        model = OrderItem
        fields = []
