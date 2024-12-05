from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from django.db.models import Q
from django.forms import ModelForm

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'User Name', 'required': 'True', 'name': 'username', 'id': "registerName"})
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Email', 'required': 'True', 'name': 'email'})
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Password', 'required': 'True', 'name': 'password'})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Re-password', 'required': 'True', 'name': 'confirm_password',  'id': "id_password"})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email
