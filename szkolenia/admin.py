from django.contrib import admin
from .models import Dzial, Pracownik, Szkolacy, Szkolenia, Szkolenie, Lider_Dzial, Autor

@admin.register(Autor)
class LokalizacjaAutor(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('user',)


@admin.register(Dzial)
class LokalizacjaDzial(admin.ModelAdmin):
    list_display = ('dzial','aktywny')
    list_filter = ('dzial','aktywny')
    search_fields = ('dzial','aktywny')


@admin.register(Pracownik)
class LokalizacjaPracownik(admin.ModelAdmin):
    list_display = ('nr_pracownika','imie','nazwisko','dzial','szkolacy','zatrudniony')
    list_filter = ('nr_pracownika','imie','nazwisko','dzial','szkolacy','zatrudniony')
    search_fields = ('nr_pracownika','imie','nazwisko','dzial','szkolacy','zatrudniony')


@admin.register(Szkolacy)
class LokalizacjaSzkolacy(admin.ModelAdmin):
    list_display = ('user','dzial')
    list_filter = ('user','dzial')
    search_fields = ('user','dzial')


@admin.register(Szkolenia)
class LokalizacjaSzkolenia(admin.ModelAdmin):
    list_display = ('data_szkolenia','czas_szkolenia','temat','opis','szkolacy','data_dodania')
    list_filter = ('data_szkolenia','czas_szkolenia','temat','opis','szkolacy','data_dodania')
    search_fields = ('data_szkolenia','czas_szkolenia','temat','opis','szkolacy','data_dodania')


@admin.register(Szkolenie)
class LokalizacjaSzkolenie(admin.ModelAdmin):
    list_display = ('uczestnik','szkolenie')
    list_filter = ('uczestnik','szkolenie')
    search_fields = ('uczestnik','szkolenie')


@admin.register(Lider_Dzial)
class LokalizacjaLider_dzial(admin.ModelAdmin):
    list_display = ('user','dzial')
    list_filter = ('user','dzial')
    search_fields = ('user','dzial')

