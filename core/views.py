"""Views for Core."""

from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.base import ContextMixin
from django.views.generic.detail import DetailView

from .models import (SiteData, ContentManagmentSystem)
from blog.models import Article


class WebsiteCommonMixin(ContextMixin):
    """This class is to apply herency and overload the get_context_data
    method and pass common site information to all views."""
    def get_context_data(self, **kwargs):
        context = super(WebsiteCommonMixin, self).get_context_data(**kwargs)
        context['site'] = SiteData.objects.order_by('-created_at')[0]
        return context


# Create your views here.
class Home(View):
    """View to home."""

    template_name = 'core/home.html'

    def get(self, request):
        """Get method"""
        return render(
            request,
            self.template_name,
            {
                'site':
                    SiteData.objects.order_by('-created_at')[0],
                'articles':
                    Article.objects.filter().order_by('-created_at')[:8]
            }
        )


class ContentManagment(WebsiteCommonMixin, DetailView):
    model = ContentManagmentSystem


def view_404(request, exception=None):
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    return redirect('/')
