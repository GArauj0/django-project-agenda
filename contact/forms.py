from utils.validators import phone_validator
from django import forms
from . import models
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )
    
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone', 'email', 'description',
            'category', 'picture'
        )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not phone_validator.search(phone): # type: ignore
            self.add_error(
                'phone',
                ValidationError(
                    'This phone number is invalid.',
                    code='invalid'
                )
            )

        return phone
    
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True
    )
    last_name = forms.CharField(
        required=True
    )
    email = forms.EmailField(
        required=True
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'This email is already registered.', code='invalid'
                    )
            )

        return email