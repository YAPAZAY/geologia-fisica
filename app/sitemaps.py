import imp
from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Article
from registration.models import Profile


class Site:
    domain = settings.DOMAIN


class StaticSitemap(Sitemap):
    protocol = settings.PROTOCOL
    priority = 1.0
    changefreq = 'never'
    
    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(StaticSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return ['core:home', ]

    def location(self, item):
        return reverse(item)


class ArticlesSitemap(Sitemap):
    protocol = settings.PROTOCOL
    priority = 0.5
    changefreq = 'never'

    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(ArticlesSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return Article.objects.filter()
    
    def location(self, item):
        return f'/{item.publication_type}/{item.slug}'

    def lastmod(self, obj):
        return obj.updated_at


class CollaboratorsSitemap(Sitemap):
    protocol = settings.PROTOCOL
    priority = 0.5
    changefreq = 'never'

    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(CollaboratorsSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return Profile.objects.filter()
    
    def location(self, item):
        return f'/academicos/{item.user.username}'
