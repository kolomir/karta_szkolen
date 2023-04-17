from django.urls import path
from .views import ostatnie_wpisy,login_request,logout_request,nowy_dzial,edytuj_dzial,wpisyDzialy,usun_dzial,przywroc_dzial, \
    nowy_pracownik, edytuj_pracownik, wpisyPracownik, usun_pracownik, przywroc_pracownik, przypisz_lider_dzial, wpisy_lider_dzial

urlpatterns = [
    path('', ostatnie_wpisy, name='ostatnie_wpisy'),

    # - Nowy ----------------------------------------------------------------
    path('dzial_form/', nowy_dzial, name='dzial_form'),
    path('pracownikForm/', nowy_pracownik, name='pracownikForm'),
    path('przypisz_lider_dzial/', przypisz_lider_dzial, name='przypisz_lider_dzial'),
    # - Edycja --------------------------------------------------------------
    path('dzialyFormedytuj/<int:id>/', edytuj_dzial, name='dzialyFormedytuj'),
    path('pracownikFormedytuj/<int:id>/', edytuj_pracownik, name='pracownikFormedytuj'),
    # - Zestawienie ---------------------------------------------------------
    path('dzialy/', wpisyDzialy, name='dzialy'),
    path('pracownik/', wpisyPracownik, name='pracownik'),
    path('lider_dzial/', wpisy_lider_dzial, name='lider_dzial'),
    # - Kasowanie -----------------------------------------------------------
    path('usun_dzial/<int:id>/', usun_dzial, name='usun_dzial'),
    path('usun_pracownik/<int:id>/', usun_pracownik, name='usun_pracownik'),
    # - Przywracanie --------------------------------------------------------
    path('przywroc_dzial/<int:id>/', przywroc_dzial, name='przywroc_dzial'),
    path('przywroc_pracownik/<int:id>/', przywroc_pracownik, name='przywroc_pracownik'),
    # - SYSTEM --------------------------------------------------------------
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
]