from django import forms
from website.models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class NewsLettersForms(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'
