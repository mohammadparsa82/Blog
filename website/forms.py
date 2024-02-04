from django import forms
from website.models import *
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'

class NewsLettersForms(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'

