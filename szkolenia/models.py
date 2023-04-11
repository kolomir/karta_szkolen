from django.db import models
from django.contrib.auth.models import User


class Dzial(models.Model):
    dzial = models.CharField(max_length=20, unique=True)
    aktywny = models.BooleanField(default=True)

    def __str__(self):
        return self.dzial


class Pracownik(models.Model):
    nr_pracownika = models.DecimalField(max_digits=4,decimal_places=0, unique=True)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=40)
    dzial = models.ForeignKey(Dzial, on_delete=models.CASCADE)
    zatrudniony = models.BooleanField(default=True)

    def __str__(self):
        return "({}) {} {}".format(self.nr_pracownika.__str__(),self.imie,self.nazwisko)


class Lider_Dzial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lider")
    dzial = models.ForeignKey(Dzial, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.user.__str__(), self.dzial.__str__())


class Szkolacy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="szkolacy")
    dzial = models.ForeignKey(Dzial, on_delete=models.CASCADE)

    def __int__(self):
        return self.user


class Szkolenia(models.Model):
    data_szkolenia = models.DateField('data szkolenia') #dzień w którym było szkolenie
    czas_szkolenia = models.TimeField('czas szkolenia') #jak długo trwało szkolenie
    temat = models.CharField(max_length=250)
    opis = models.CharField(max_length=2500)
    szkolacy = models.ForeignKey(Szkolacy, on_delete=models.CASCADE)
    data_dodania = models.DateField('data dodania', blank=True, null=True)

    def __str__(self):
        return self.temat


class Szkolenie(models.Model): #klasa przypisuje do szkolenia jej uczestników
    uczestnik = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    szkolenie = models.ForeignKey(Szkolenia, on_delete=models.CASCADE)

    def __str__(self):
        return self.dzial.__str__()
