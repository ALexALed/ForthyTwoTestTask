# - *- coding: utf- 8 - *-
__author__ = 'alexaled'
from django.forms import ModelForm, Textarea
from models import MyBio

class MyBioForm(ModelForm):
    class Meta:
        model = MyBio
        fields = "__all__"
        widgets = {
            'biography': Textarea(attrs={'cols': 30, 'rows': 10}),
            'other_contacts': Textarea(attrs={'cols': 30, 'rows': 10}),
        }