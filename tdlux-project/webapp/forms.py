from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={}), label="Повторите пароль",)
    class Meta():
        model = User
        fields = ('name', 'username', 'email', 'phone', 'adress', 'password')
        widgets = {
            # telling Django your password field in the mode is a password input on the template
            'password': forms.PasswordInput() 
            
        }