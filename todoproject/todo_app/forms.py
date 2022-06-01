from .models import remainder
from django import forms

class form(forms.ModelForm):
    class Meta:
        model=remainder
        fields=['name','priority','date']