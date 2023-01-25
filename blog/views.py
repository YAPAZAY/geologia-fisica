import random

from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Article
from .forms import ArticleForm
from core.views import WebsiteCommonMixin
from registration.decorators import is_approved, is_author


class ArticleListView(WebsiteCommonMixin, ListView):
    model = Article
    ordering = ['title']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = Article.objects.order_by(
            'subject').values_list('subject', flat=True).distinct()

        context['subject'] = subject
        return context

    def get_queryset(self):
        articles = Article.objects.all()

        if self.kwargs.get('publication_type'):
            articles = articles.filter(
                publication_type=self.kwargs['publication_type'])
            if len(articles) == 0:
                raise Http404()

        return articles


class ArticleDetailView(WebsiteCommonMixin, DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = self.get_articles()
        context['is_author'] = self.check_author()

        return context

    def get_articles(self):
        articles = Article.objects.filter(
            author=self.object.author
        ).exclude(
            title=self.object.title
        )
        articles = list(articles)
        random.shuffle(articles)

        return articles
    
    def check_author(self):
        slug = self.request.resolver_match.kwargs['slug']
        author = str(Article.objects.filter(slug=slug)[0].author).strip()
        return author == self.request.user.username.strip()


@method_decorator(is_approved, name='dispatch')
class ArticleCreate(WebsiteCommonMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:article', args=[
            self.object.publication_type, self.object.slug
        ]) + '?ok'


@method_decorator(is_author, name='dispatch')
class ArticleUpdate(WebsiteCommonMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'

    def get_success_url(self):
        print('en la vista')
        return reverse_lazy('blog:update', args=[
            self.object.publication_type, self.object.slug
        ]) + '?ok'



@method_decorator(is_author, name='dispatch')
class ArticleDelete(WebsiteCommonMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('blog:article')
