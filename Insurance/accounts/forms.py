from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm

User = get_user_model()


class LoginForm(AuthenticationForm):
    class Meta:
        username = forms.CharField(max_length=255, help_text='Username or Email Address')
        model = User
        fields = ['username', 'password']


class PasswordChange(PasswordChangeForm):
    class Meta:
        widgets = {

        }
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField(initial=263)

    class Meta:
        widgets = {
            'password': forms.PasswordInput(),
        }

        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'id_number', 'province', 'nationality',
                  'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'username']
