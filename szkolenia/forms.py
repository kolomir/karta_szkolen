from django.forms import ModelForm
from django import forms
from .models import Dzial

'''
Dzial
-----------------------------------------------------------------------------------------------------------------------
'''
class DzialForm(ModelForm):
    class Meta:
        model = Dzial
        fields = ['dzial','aktywny']


class SkasowacDzial(ModelForm):
    class Meta:
        model = Dzial
        fields = [
            'aktywny',
        ]