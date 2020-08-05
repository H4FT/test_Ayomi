from django import forms

class modal(forms.Form):
    change_email = forms.CharField(label='Email', max_length=200)