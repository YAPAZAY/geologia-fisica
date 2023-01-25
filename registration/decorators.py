from django.http import HttpResponseForbidden

from blog.models import Article


def is_approved(view_func):
    """Decorator to avoid an non-approved user to create blog entries"""
    def wrap(request, *args, **kwargs):
        try:
            if request.user.profile.approved:
                return view_func(request, *args, **kwargs)
        
        except (AttributeError):
            pass
        
        return HttpResponseForbidden()

    return wrap


def is_author(view_func):
    """Decorator to avoid an non-author user to edit or delete blog entries"""
    def wrap(request, *args, **kwargs):
        slug = request.resolver_match.kwargs['slug']
        author = str(Article.objects.filter(slug=slug)[0].author).strip()
        is_author = author == request.user.username.strip()
        try:
            if request.user.profile.approved and is_author:
                return view_func(request, *args, **kwargs)
        
        except AttributeError:
            pass
        
        return HttpResponseForbidden()
    
    return wrap
