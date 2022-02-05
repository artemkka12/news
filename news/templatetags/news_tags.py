from django import template
from django.db.models import Count
from django.contrib.auth.models import User

from news.models import Category, News

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.filter(news__is_published=True).annotate(cnt=Count('news')).order_by('-cnt')


@register.simple_tag(name='get_list_authors')
def get_authors():
    return User.objects.filter(news__is_published=True).annotate(cnt=Count('news')).order_by('-cnt')


@register.simple_tag(name='get_list_popular_news')
def get_popular_news():
    return News.objects.order_by('-views')[:3]
