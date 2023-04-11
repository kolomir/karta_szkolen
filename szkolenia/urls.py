from django.urls import path
from .views import ostatnie_wpisy,login_request,logout_request,nowy_dzial,edytuj_dzial,wpisyDzialy,usun_dzial,przywroc_dzial

urlpatterns = [
    path('', ostatnie_wpisy, name='ostatnie_wpisy'),

    # - Nowy ----------------------------------------------------------------
    path('dzial_form/', nowy_dzial, name='dzial_form'),
    # - Edycja --------------------------------------------------------------
    path('dzialyFormedytuj/<int:id>/', edytuj_dzial, name='dzialyFormedytuj'),
    # - Zestawienie ---------------------------------------------------------
    path('dzialy/', wpisyDzialy, name='dzialy'),
    # - Kasowanie -----------------------------------------------------------
    path('usun_dzial/<int:id>/', usun_dzial, name='usun_dzial'),
    # - Przywracanie --------------------------------------------------------
    path('przywroc_dzial/<int:id>/', przywroc_dzial, name='przywroc_dzial'),
    # - SYSTEM --------------------------------------------------------------
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
]