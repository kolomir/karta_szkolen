from django.shortcuts import render, redirect, get_object_or_404
from .models import Szkolenia, Dzial, Pracownik, Autor, Lider_Dzial
from .forms import DzialForm, SkasowacDzial, PracownikForm, SkasowacPracownik, LiderDzial
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


'''
Inne
-----------------------------------------------------------------------------------------------------------------------
'''
def get_author(user):
    qs = Autor.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None
# ---------------------------------------------------------------------------------------------------------------------


'''
Ostatnie wpisy
-----------------------------------------------------------------------------------------------------------------------
'''
def ostatnie_wpisy(request):
    ostatnie_szkolenia = Szkolenia.objects.all().order_by('-id')[:50]

    context = {
        'ostatnie_szkolenia': ostatnie_szkolenia
    }
    return render(request, 'szkolenia/ostatnie.html', context)
# ---------------------------------------------------------------------------------------------------------------------


'''
Pracownik
-----------------------------------------------------------------------------------------------------------------------
'''
@login_required
def nowy_pracownik(request):
    form_pracownik = PracownikForm(request.POST or None, request.FILES or None)
    dzial = Dzial.objects.filter(aktywny=True).order_by('dzial')

    serw = request.POST.get('szkolacy')
    if serw == 'on':
        szkolacy = True
    else:
        szkolacy = False

    if form_pracownik.is_valid():
        form_pracownik.instance.szkolacy = szkolacy
        form_pracownik.save()
        return redirect(wpisyPracownik)

    context = {
        'form_pracownik': form_pracownik,
        'dzial': dzial
    }

    return render(request, 'szkolenia/form_pracownik.html', context)


@login_required
def edytuj_pracownik(request, id):
    wpis = get_object_or_404(Pracownik, pk=id)
    dzial = Dzial.objects.filter(aktywny=True).order_by('dzial')
    form_pracownik = PracownikForm(request.POST or None, request.FILES or None, instance=wpis)

    serw = request.POST.get('szkolacy')
    if serw == 'on':
        szkolacy = True
    else:
        szkolacy = False

    if form_pracownik.is_valid():
        form_pracownik.instance.szkolacy = szkolacy
        form_pracownik.save()
        return redirect(wpisyPracownik)

    context = {
        'form_pracownik': form_pracownik,
        'wpis': wpis,
        'dzial': dzial
    }

    return render(request, 'szkolenia/form_pracownik_ed.html', context)


@login_required
def usun_pracownik(request, id):
    wpis = get_object_or_404(Pracownik, pk=id)
    form_wpis = SkasowacPracownik(request.POST or None, request.FILES or None, instance=wpis)

    if form_wpis.is_valid():
        kasuj = form_wpis.save(commit=False)
        kasuj.zatrudniony = 0
        kasuj.save()
        return redirect(wpisyPracownik)

    context = {
        'wpis': wpis
    }
    return render(request, 'szkolenia/potwierdz_pracownik.html', context)


@login_required
def przywroc_pracownik(request, id):
    wpis = get_object_or_404(Pracownik, pk=id)
    form_wpis = SkasowacPracownik(request.POST or None, request.FILES or None, instance=wpis)

    if form_wpis.is_valid():
        kasuj = form_wpis.save(commit=False)
        kasuj.zatrudniony = 1
        kasuj.save()
        return redirect(wpisyPracownik)

    context = {
        'wpis': wpis
    }
    return render(request, 'szkolenia/potwierdz_pracownik.html', context)


def wpisyPracownik(request):
    pracownik = Pracownik.objects.all().order_by('nr_pracownika')

    context = {
        'pracownik': pracownik
    }
    return render(request,'szkolenia/pracownik.html',context)
# ---------------------------------------------------------------------------------------------------------------------


'''
Dzial
-----------------------------------------------------------------------------------------------------------------------
'''
@login_required
def nowy_dzial(request):
    form_dzial = DzialForm(request.POST or None, request.FILES or None)

    if form_dzial.is_valid():
        form_dzial.save()
        return redirect(wpisyDzialy)

    context = {
        'form_dzial': form_dzial
    }

    return render(request, 'szkolenia/form_dzial.html', context)


@login_required
def edytuj_dzial(request, id):
    wpis = get_object_or_404(Dzial, pk=id)

    form_dzial = DzialForm(request.POST or None, request.FILES or None, instance=wpis)

    if form_dzial.is_valid():
        form_dzial.save()
        return redirect(wpisyDzialy)

    context = {
        'form_dzial': form_dzial,
        'wpis': wpis
    }

    return render(request, 'szkolenia/form_dzial_ed.html', context)


@login_required
def usun_dzial(request, id):
    wpis = get_object_or_404(Dzial, pk=id)
    form_wpis = SkasowacDzial(request.POST or None, request.FILES or None, instance=wpis)

    if form_wpis.is_valid():
        kasuj = form_wpis.save(commit=False)
        kasuj.aktywny = 0
        kasuj.save()
        return redirect(wpisyDzialy)

    context = {
        'wpis': wpis
    }
    return render(request, 'szkolenia/potwierdz_dzial.html', context)


@login_required
def przywroc_dzial(request, id):
    wpis = get_object_or_404(Dzial, pk=id)
    form_wpis = SkasowacDzial(request.POST or None, request.FILES or None, instance=wpis)

    if form_wpis.is_valid():
        kasuj = form_wpis.save(commit=False)
        kasuj.aktywny = 1
        kasuj.save()
        return redirect(wpisyDzialy)

    context = {
        'wpis': wpis
    }
    return render(request, 'szkolenia/potwierdz_dzial.html', context)


def wpisyDzialy(request):
    dzialy = Dzial.objects.all().order_by('dzial')

    context = {
        'dzialy': dzialy
    }
    return render(request,'szkolenia/dzialy.html',context)
# ---------------------------------------------------------------------------------------------------------------------


'''
Lider <-> Dział
-----------------------------------------------------------------------------------------------------------------------
'''
@login_required
def przypisz_lider_dzial(request):
    form_lider_dzial = LiderDzial(request.POST or None, request.FILES or None)
    lider_user = Autor.objects.all()
    dzial = Dzial.objects.filter(aktywny=True).order_by('dzial')
    print(lider_user)

    if form_lider_dzial.is_valid():
        get_lider = request.POST.get('lider_user')
        print(get_lider)
        form_lider_dzial.save()
        return redirect(wpisy_lider_dzial)

    context = {
        'form_lider_dzial': form_lider_dzial,
        'lider_user': lider_user,
        'dzial': dzial,
    }

    return render(request, 'szkolenia/form_lider_dzial.html', context)

# TODO: Dodać jeszcze edycję, kasowanie i i przywracanie. Linki w szablonie HTML są niepoprawne w tej chwili.

def wpisy_lider_dzial(request):
    lider_dzial = Lider_Dzial.objects.all().order_by('user')

    context = {
        'lider_dzial': lider_dzial
    }
    return render(request,'szkolenia/lider_dzial.html',context)
# ---------------------------------------------------------------------------------------------------------------------


'''
Logout
-----------------------------------------------------------------------------------------------------------------------
'''
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info( request, f"Witaj {username}! Właśnie się zalogowałeś.")
                return redirect("/")
            else:
                messages.error(request, f"Błędny login lub hasło")
        else:
            messages.error(request, f"- Błędny login lub hasło -")
    form = AuthenticationForm()

    context = {
        "form": form
    }
    return render(request, "szkolenia/login.html", context)
# ---------------------------------------------------------------------------------------------------------------------


'''
Logout
-----------------------------------------------------------------------------------------------------------------------
'''
def logout_request(request):
    logout(request)
    messages.info(request, "Właśnie się wylogowałeś")
    return redirect(ostatnie_wpisy)
# ---------------------------------------------------------------------------------------------------------------------