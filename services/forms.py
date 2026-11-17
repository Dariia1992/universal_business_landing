from django import forms
from .models import ContactRequest


class ContactRequestModelForm(forms.ModelForm):
    class Meta:
        model = ContactRequest #model iz models
        fields = ('name','email','phone','message')
        labels = {
            'name': "name",
            'email': "email",
            'phone': "phone",
            'message': "message",
           
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Enter name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter phone'}),
            'message': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Enter message'}),
           
        }
        


