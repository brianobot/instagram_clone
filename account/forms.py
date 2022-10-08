from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from .models import Profile, User

import logging
logger = logging.getLogger(__name__)

class CustomUserCreationForm(UserCreationForm):
    """ 
    Extends the UserCreationForm to add the email field as a field to be used in the form
    """
    error_css_class = 'error'
    required_css_class = 'required'

    class Meta(UserCreationForm.Meta):
        model = User
        # review - pack the minimal no of fields to get just enuf data about a useron creation
        fields = ('email',)

        widgets = {
            "password1": forms.PasswordInput(attrs={'autocomplete': 'off'}),
            "password2": forms.PasswordInput(attrs={'autocomplete': 'off'}),
        }

    def send_sms(self):
        # review implement sms sending to users to alert and welcome them to the system
        pass

    def clean(self):
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if (email is not None) and (password1 is not None) and (password2 is not None):
            used_email = User.objects.filter(email=email).exists()
            if used_email:
                raise forms.ValidationError("Email has already been used")
        return self.cleaned_data


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)


class AuthenticationForm(forms.Form):
    """
    bla bla bla documentated by aiddee
    """
    email = forms.CharField(max_length=255, help_text=_('Enter Email address'), label="Email address")
    password = forms.CharField(min_length=5, max_length=255, strip=False, widget=forms.PasswordInput, help_text=_('Enter Password'))

    widgets = {
        'email': forms.TextInput(attrs={'placeholder': 'Email address'}),
        'password': forms.PasswordInput(attrs={'placeholder': 'Password'})
    }

    def __init__(self, request, *args, **kwargs):
        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        
        if email is not None and password:
            self.user = authenticate(self.request, email=email, password=password) 

            if self.user is None:
                logger.warn(f"Authentication failed for email = {email or 'blank'}")
                raise ValidationError("Invalid email and password combination")
            logger.info(f"Authentication successful for email = {email}")
            messages.success(self.request, f"Welcome back! it has been a minute... <a href='/explore'>check out what you missed 🔎</a>")
        
        return self.cleaned_data

    def get_user(self):
        return self.user


class SimpleProfileSetting(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('handle', 'avatar')