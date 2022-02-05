from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    content = models.TextField(blank=True, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date edited')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo', blank=True, null=True)
    is_published = models.BooleanField(default=False, verbose_name='Publish')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='news')
    members = models.ManyToManyField(User, related_name='members', blank=True)

    def get_absolute_url(self):
        return reverse('view-news', kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='name of category')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-title']
