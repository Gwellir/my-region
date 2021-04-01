from django import forms
from django.forms import SelectDateWidget

from .models import RouteType, RouteLevel, Route, District, Region


class RouteFilterForm(forms.Form):
    """
    Реализация формы фильтра для первого MVP.
    """
    # name = forms.CharField(label='Название', max_length=100, required=False)
    district = forms.ModelChoiceField(queryset=District.objects.all(),
                                      label='Округ',
                                      required=False,
                                      empty_label='Округ'
                                      )
    region = forms.ModelChoiceField(queryset=Region.objects.all(),
                                    label='Регион',
                                    empty_label='Регион',
                                    required=False)
    type = forms.ChoiceField(
        label='Тип маршрута',
        choices=[('', 'Тип маршрута')] + [(x, x.label) for x in RouteType],
        required=False,
    )
    level = forms.ChoiceField(
        label='Сложность',
        choices=[('', 'Сложность')] + [(x, x.label) for x in RouteLevel],
        required=False,
    )
    date_from = forms.DateField(label='Дата начала', required=False,
                                widget=SelectDateWidget())
    date_to = forms.DateField(label='Дата окончания', required=False,
                              widget=SelectDateWidget())
    price_from = forms.DecimalField(label='Цена от', required=False)
    price_to = forms.DecimalField(label='Цена до', required=False)


class RouteCreateForm(forms.ModelForm):
    """
    Форма создания маршрута.
    """
    photos = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Route
        fields = ['name', 'route_type', 'base_price', 'short_desc', 'long_desc', 'location',
                  'duration', 'length', 'complexity', 'featured_photo', 'photos', 'gpx_track']
