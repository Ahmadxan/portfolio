from django.urls import path
from . import views
from django.contrib.auth.decorators import permission_required

urlpatterns = [
    path('article/list/', views.ArticleListView.as_view(), name='article-list'),
    path('article/create/', views.ArticleCreateView.as_view(), name='article-create'),
    path('article/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article-update'),
    path('article/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article-delete'),

    path('video/list/', views.VideoListView.as_view(), name='video-list'),
    path('video/create/', views.VideoCreateView.as_view(), name='video-create'),
    path('video/<int:pk>/edit/', views.VideoUpdateView.as_view(), name='video-update'),
    path('video/<int:pk>/delete/', views.VideoDeleteView.as_view(), name='video-delete'),
]
