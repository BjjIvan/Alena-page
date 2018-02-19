from django import forms
from .models import SignUp, UserprofileInfo
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model= SignUp
        fields = ['full_name','email']
    def clead_email(self):
        email = self.cleaned_data.get('email')
        email_base,provider = email.split('@')
        domain, extension = provider.split('.')
        if not extension =='edu':
            raise forms.ValidationError('Please use a valid .edu email adress')
        return email


class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ['username','email','password']

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserprofileInfo
        fields = ['portfolio_site','profile_pic']
