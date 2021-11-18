from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)
from articles.models import Article, Video, Comment
from account.models import Message, Contact


class HomePageView(ListView):
    model = Article
    template_name = 'home.html'


class ArticlePageView(ListView):
    model = Article
    paginate_by = 12
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


def portfolio_page(request):
    model = Message()
    if request.POST:
        model.name = request.POST.get('name')
        model.tell = request.POST.get('tell')
        model.email = request.POST.get('email')
        model.message = request.POST.get('message')
        model.save()
    print(model)
    return render(request, 'index.html')


class VideoPageView(ListView):
    model = Video
    paginate_by = 12
    template_name = 'video_list.html'


def contact_page(request):
    model = Contact()
    if request.POST:
        model.name = request.POST.get('name')
        model.email = request.POST.get('email')
        model.subject = request.POST.get('subject')
        model.message = request.POST.get('message')
        model.save()
    return render(request, 'contact.html')


class AdminPageView(ListView):
    model = Comment
    template_name = 'dashboard/index.html'


class SearchArticle(ListView):
    template_name = 'search.html'

    def get_queryset(self):
        return Article.objects.filter(title__icontains=self.request.GET.get("s")) or Video.objects.filter(
            title__icontains=self.request.GET.get("s"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["s"] = self.request.GET.get("s")
        return context
