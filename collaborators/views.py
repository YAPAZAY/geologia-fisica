from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blog.models import Article
from core.views import WebsiteCommonMixin
from registration.models import Profile


class CollaboratorListView(WebsiteCommonMixin, ListView):
    model = Profile
    template_name = 'collaborators/collaborator_list.html'


class CollaboratorDetailView(WebsiteCommonMixin, DetailView):
    model = Profile
    template_name = 'collaborators/collaborator_detail.html'

    def get_object(self):
        return get_object_or_404(
            Profile, user__username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.filter(
            author=self.object.user
        )
        context['articles'] = articles

        return context
