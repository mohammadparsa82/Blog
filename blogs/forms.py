from django import forms
from blogs.models import *
from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):
    #captcha = CaptchaField()
    class Meta:
        model = comment
        fields = ['post','name' , 'email', 'subject' , 'message', ]

