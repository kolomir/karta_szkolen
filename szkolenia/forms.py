from django.forms import ModelForm
from django import forms
from .models import Dzial, Pracownik, Lider_Dzial

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


'''
Pracownik
-----------------------------------------------------------------------------------------------------------------------
'''
class PracownikForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PracownikForm, self).__init__(*args, **kwargs)
        self.fields['dzial'] = forms.ModelChoiceField(queryset=Dzial.objects.filter(aktywny=True))

    class Meta:
        model = Pracownik
        fields = ['nr_pracownika','imie','nazwisko','dzial','zatrudniony']


class SkasowacPracownik(ModelForm):
    class Meta:
        model = Pracownik
        fields = [
            'zatrudniony',
        ]


'''
Pracownik
-----------------------------------------------------------------------------------------------------------------------
'''
class LiderDzial(ModelForm):
    class Meta:
        model = Lider_Dzial
        fields = ['user','dzial']