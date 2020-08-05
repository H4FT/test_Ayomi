from django import forms

class identif_mail(forms.Form):
    mail = forms.CharField(label='Email', max_length=200)

class identif_name(forms.Form):
    name = forms.CharField(label='Name', max_length=200)