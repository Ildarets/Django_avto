from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label = "Название")
    email = forms.EmailField(label = 'email')
    massage = forms.CharField(label = 'Сообщение')