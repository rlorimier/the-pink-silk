from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Form for Contact model that uses all fields """

    class Meta:
        model = Contact
        fields = ['full_name', 'email_address', 'message']
