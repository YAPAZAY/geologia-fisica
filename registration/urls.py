from django.urls import path
from .views import ProfileUpdate, SignUpView, LoginView


urlpatterns = [
    path('mi-perfil', ProfileUpdate.as_view(), name='my-profile'),
    path('registro/', SignUpView.as_view(), name='sign-up'),
    path('login/', LoginView.as_view(), name='login')
]
