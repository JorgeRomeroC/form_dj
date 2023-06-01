from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre y Apellido', max_length=25, min_length=5, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Introduzca los datos'}))

    email = forms.EmailField(label='Correo Electronico', required=True, max_length=100,
                            widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electronico'}))

    message = forms.CharField(label='Mensaje', required=True,
                            widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensaje', 'rows': 5}))