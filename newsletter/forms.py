__author__ = 'felipe'
from django import forms
from .models import SignUp

class ContactForm(forms.Form):
    nome = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "edu" in email:
            raise forms.ValidationError('Entre com um e-mail .edu valido')
        return email

    # def clean_nome(self):
    #     nome = self.cleaned_data.get('nome')
    #     if not "Felipe" in nome:
    #         raise forms.ValidationError("Seu nome não é Felipe!")
    #     return nome

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['Nome', 'email']
        # exclude = ['full_name']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "edu" in email:
            raise forms.ValidationError('Entre com um e-mail .edu valido')
        return email

    def clean_nome(self):
        nome = self.cleaned_data.get('Nome')
