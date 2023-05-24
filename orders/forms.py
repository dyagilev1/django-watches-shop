from django import forms
from .models import Order
from django.contrib.auth.models import User


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(label="Ім'я", widget = forms.TextInput(attrs={"placeholder":"Ім'я",'class':'form-control'}))
    last_name = forms.CharField(label="Прізвище", widget = forms.TextInput(attrs={"placeholder":"Прізвище",'class':'form-control'}))
    email = forms.EmailField(label="E-mail", widget = forms.EmailInput(attrs={"placeholder":"E-mail",'class':'form-control'}))
    address = forms.CharField(label="Адреса", widget = forms.TextInput(attrs={"placeholder":"Адреса",'class':'form-control'}))
    city = forms.CharField(label="Місто", widget = forms.TextInput(attrs={"placeholder":"Місто",'class':'form-control'}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'city']