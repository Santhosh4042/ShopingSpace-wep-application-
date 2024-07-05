from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomerForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'})) 
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email Address'})) 
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'})) 
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Reenter Your Password'})) 
    class Meta: 
        model = User
        fields = ['username','email','password1','password2']
 