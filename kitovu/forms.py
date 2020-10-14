from django import forms
from django.forms import ModelForm


from kitovu.models import post_form


class post_form(forms.ModelForm):
    class Meta:
        model = post_form
        fields = ['author','phone','message']
