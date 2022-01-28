from django import template
from django.db.models import Count, Max

from news.models import Category, News

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    categories = Category.objects.filter(news__is_published=True).annotate(cnt=Count('news')).order_by('-cnt')
    return categories


@register.simple_tag(name='get_list_popular_news')
def get_popular_news():
    popular_news = News.objects.order_by('-views')
    return popular_news[:3]


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {"categories": categories}
