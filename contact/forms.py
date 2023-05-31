from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre y Apellido', max_length=25, min_length=5, required=True)
    email = forms.CharField(max_length=)
    message = forms.CharField(max_length=)