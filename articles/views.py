
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Article, Comment, Video
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Article views

class ArticleListView(ListView):
    model = Article
    template_name = 'dashboard/article/list.html'


class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    fields = ('title', 'summery', 'body', 'image', 'manba')
    template_name = 'dashboard/article/article_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'summery', 'body', 'image', 'author', 'manba')
    template_name = 'dashboard/article/article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'dashboard/article/article_delete.html'
    success_url = reverse_lazy('article-list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


# Video views

class VideoListView(ListView):
    model = Video
    template_name = 'dashboard/video/list.html'


class VideoCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Video
    fields = ('title', 'summery', 'video', 'manba')
    template_name = 'dashboard/video/video_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class VideoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Video
    fields = ('title', 'summery', 'video', 'author', 'manba')
    template_name = 'dashboard/video/video_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class VideoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Video
    template_name = 'dashboard/video/video_delete.html'
    success_url = reverse_lazy('video-list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user