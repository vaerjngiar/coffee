from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'sender', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Type your name'}),
            'sender': forms.TextInput(attrs={'placeholder': 'Type your email'}),

        }
