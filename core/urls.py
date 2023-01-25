from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('cms/<slug:slug>/', views.ContentManagment.as_view(), name='cms'),
]
