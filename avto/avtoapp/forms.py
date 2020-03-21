from django import forms
from .models import Avto

class ContactForm(forms.Form):
    name = forms.CharField(label = "Название")
    email = forms.EmailField(label = 'email')
    massage = forms.CharField(label = 'Сообщение')

class PostForm(forms.ModelForm):
    class Meta:
        model = Avto
        fields = '__all__'
        