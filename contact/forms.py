from utils.validators import phone_validator
from django import forms
from . import models
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone', 'email', 'description',
            'category',
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