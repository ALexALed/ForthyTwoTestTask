# - *- coding: utf- 8 - *-
__author__ = 'alexaled'
from django.forms import ModelForm, Textarea, DateField, TextInput
from models import MyBio


class CalendarWidget(TextInput):

    class Media:
        js = ('/static/js/jquery-1.11.1.min.js',
              '/static/js/jquery-ui.min.js')
        css = {'all': '/static/css/jquery-ui.min.css'}


class MyBioForm(ModelForm):
    birth_date = DateField(widget=CalendarWidget)

    class Meta:
        model = MyBio
        fields = "__all__"
        widgets = {
            'biography': Textarea(attrs={'cols': 30, 'rows': 10}),
            'other_contacts': Textarea(attrs={'cols': 30, 'rows': 10}),
        }
