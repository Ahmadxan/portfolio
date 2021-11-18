from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=200)
    summery = models.CharField(max_length=300, blank=True)
    body = RichTextField()
    image = models.FileField(upload_to="images/", blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    manba = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-list')


class Video(models.Model):
    title = models.CharField(max_length=200)
    summery = models.CharField(max_length=200, blank=True, null=True)
    video = models.FileField(upload_to="file/")
    author = models.ForeignKey(get_user_model(), models.CASCADE, blank=True, null=True)
    manba = models.CharField(max_length=300, blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('video-list')


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    full_name = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('article_detail')