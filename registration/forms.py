from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, UsernameField)
from django.contrib.auth.models import User

from .models import Profile


class UserCreationFormExtended(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name',
            'email', 'password1', 'password2'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Este correo electrónico ya fue registrado")

        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'avatar', 'occupation',
            'institution', 'bio'
        )

        widgets = {
            'avatar': forms.ClearableFileInput(
                attrs={'class': 'file-input'}
            ),
            'occupation': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'Ej. Profesor de Asignatura A'
                }
            ),
            'institution': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'Ej. Insituto de Ingeniería, UNAM'
                }
            ),
            'bio': forms.Textarea(
                attrs={
                    'class': 'textarea',
                    'rows': 3,
                    'placeholder': 'Cuentanos lo genial que eres'}
            )
        }


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'class': 'input is-large',
                'placeholder': 'Usuario'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'input is-large',
                'placeholder': 'Contraseña'
            }
        )
    )
