from django.urls import path
from .views import CollaboratorListView, CollaboratorDetailView


urlpatterns = [
    path('', CollaboratorListView.as_view(), name='collaborators'),
    path(
        '<username>/', CollaboratorDetailView.as_view(), name='collaborator')
]
