from django import template
from django.template.defaultfilters import date as _date

register = template.Library()

@register.filter
def custom_date(value, arg):
    formatted_date = _date(value, arg)
    months = {
        'январь': 'января',
        'февраль': 'февраля',
        'март': 'марта',
        'апрель': 'апреля',
        'май': 'мая',
        'июнь': 'июня',
        'июль': 'июля',
        'август': 'августа',
        'сентябрь': 'сентября',
        'октябрь': 'октября',
        'ноябрь': 'ноября',
        'декабрь': 'декабря'
    }
    for key, value in months.items():
        formatted_date = formatted_date.replace(key, value)
    return formatted_date
