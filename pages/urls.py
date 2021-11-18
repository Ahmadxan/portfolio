from django.contrib import admin
from django.urls import path
from .views import (HomePageView,
                    portfolio_page,
                    VideoPageView,
                    contact_page,
                    AdminPageView,
                    ArticlePageView,
                    ArticleDetailView,
                    SearchArticle,
                    )
from django.contrib.auth.decorators import permission_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),

    path('maqola/', ArticlePageView.as_view(), name='article_list'),
    path('maqola/<int:pk>/detail/', ArticleDetailView.as_view(), name='article_detail'),

    path('portfolio/', portfolio_page, name='portfolio'),
    path('video/', VideoPageView.as_view(), name='video_list'),
    path('contact/', contact_page, name='contact'),

    path('maqola/search/', SearchArticle.as_view(), name='search'),
    # path('video/search/', SearchVideo.as_view(), name='search'),
]
