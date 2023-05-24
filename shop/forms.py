from django import forms
from .models import  Review

    
class ReviewForm(forms.Form):
    first_name = forms.CharField(label="Ім'я",widget=forms.TextInput(attrs={"placeholder":"Ім'я","required":True,'class':'form-control'}),error_messages={"required":"Ім'я не може бути порожнім"})
    last_name = forms.CharField(label="Прізвище",widget=forms.TextInput(attrs={"placeholder":"Прізвище","required":True,'class':'form-control'}),error_messages={"required":"Прізвище не може бути порожнім"})
    email = forms.EmailField(label="E-mail",widget=forms.EmailInput(attrs={"required":True,"Placeholder":"E-mail",'class':'form-control'}),error_messages={'required':'Поля електронної пошти не повинні бути порожніми'})
    review_text = forms.CharField(min_length=20,label="Напишіть відгук тут", widget=forms.Textarea(attrs={'placeholder': 'Напишіть відгук тут','class':'form-control'}))

    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'email', 'message']

