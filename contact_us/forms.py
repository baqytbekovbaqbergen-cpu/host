from django import forms
from .models import ContactMessage
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','email','message']

class Answerform(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['answer']