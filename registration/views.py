from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView

from .forms import UserCreationFormExtended, ProfileForm, LoginForm
from .models import Profile
from core.views import WebsiteCommonMixin


class SignUpView(WebsiteCommonMixin, CreateView):
    form_class = UserCreationFormExtended
    template_name = 'registration/sign_up.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?registro-exitoso'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        form.fields['username'].widget = forms.TextInput(
            attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Nombre de usuario'
            }
        )
        form.fields['first_name'].widget = forms.TextInput(
            attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Nombre'
            }
        )
        form.fields['last_name'].widget = forms.TextInput(
            attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Apellidos'
            }
        )
        form.fields['email'].widget = forms.EmailInput(
            attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Correo electrónico'
            }
        )
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Contraseña'
            }
        )
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Confirma tu contraseña'
            }
        )

        return form

class LoginView(WebsiteCommonMixin, LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('my-profile')


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(WebsiteCommonMixin, UpdateView):
    form_class = ProfileForm
    template_name = 'registration/profile_form.html'
    success_url = reverse_lazy('my-profile')

    def get_object(self):
        profile, _ = Profile.objects.get_or_create(user=self.request.user)
        return profile
