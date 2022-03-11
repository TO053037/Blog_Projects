from django.views.generic import ListView, DetailView, CreateView
from . import models
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse


class ArticleList(ListView):
    template_name = 'blog/index.html'
    model = models.Article

    def get_good_article_list(self):
        good_article_list = []
        article_list = models.Article.objects.filter(is_public=True)
        for article in article_list:
            if self.request.user in article.good_user.all():
                good_article_list.append(article)
        return good_article_list

    def get_context_data(self, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        context.update({
            'article_list': models.Article.objects.filter(is_public=True),
            'good_article_list': self.get_good_article_list(),
        })
        return context


class ArticleDetail(DetailView):
    template_name = 'blog/detail.html'
    model = models.Article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        article = get_object_or_404(models.Article, id=self.kwargs['pk'], is_public=True)
        context.update({
            'comments': models.Comment.objects.filter(article=article),
            'good_cnt': article.good_user.all().count(),
        })
        print(article.good_user.all())

        return context

    def get_queryset(self):
        return models.Article.objects.filter(is_public=True)


class CreateCommentView(CreateView):
    template_name = 'blog/create_comment.html'
    model = models.Comment
    fields = ['content']

    def get_success_url(self, **kwargs):
        return reverse('detail_article', kwargs={'pk': self.kwargs['article_pk']})

    def form_valid(self, form, **kwargs):
        form = form.save(commit=False)
        form.article = models.Article.objects.get(pk=self.kwargs['article_pk'])
        form.user = self.request.user
        form.save()

        return super().form_valid(form)


def do_good(request, article_pk):
    article = models.Article.objects.get(pk=article_pk)
    user = request.user
    if user in article.good_user.all():
        article.good_user.remove(user)
    else:
        article.good_user.add(user)

    return redirect('detail_article', article_pk)
