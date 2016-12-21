from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from app import views

urlpatterns = [
    url(r'^api/v1/articles$',  views.get_articles, name='get_articles'),
    url(r'^api/v1/articles/save$',  views.save_article, name='save_article'),
    url(r'^api/v1/articles/(?P<pk>[0-9]+)$', views.get_article, name='get_articles'),
    url(r'^api/v1/articles/delete/(?P<pk>[0-9]+)$', views.delete_article, name='delete_article')
]

urlpatterns = format_suffix_patterns(urlpatterns)
