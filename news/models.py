from django.db import models

from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    views = models.IntegerField(default=0)
    users_ip = models.CharField(max_length=150, default='a')

    def get_absolute_url(self):
        return reverse('view-news', kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-title']