from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import NewsForm, UserRegisterForm, UserLoginForm
from .models import News, Category


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration completed successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Registration error!')
    form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class Categories(ListView):
    model = Category
    template_name = 'news/list_categories.html'
    context_object_name = 'categories'


class Authors(ListView):
    model = User
    template_name = 'news/list_authors.html'
    context_object_name = 'authors'


class NewsByCategory(HomeNews):
    template_name = 'news/category_news_list.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs["category_id"])
        context['popular_news'] = News.objects.filter(category__title=context['title']).order_by('-views').first()
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs["category_id"], is_published=True)


class NewsByAuthor(HomeNews):
    template_name = 'news/news_by_author.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular_news'] = News.objects.filter(author_id=self.kwargs["author_id"], is_published=True).order_by(
            '-views').first()
        return context

    def get_queryset(self):
        return News.objects.filter(author_id=self.kwargs["author_id"], is_published=True)


class ViewNews(DetailView):
    def get_object(self, queryset=None):
        obj = get_object_or_404(News, pk=self.kwargs.get('pk'))

        if self.request.user.is_authenticated:
            obj.members.add(self.request.user)
            obj.views = obj.members.count()
        obj.save()

        return obj


class CreateNews(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = NewsForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('index')
    obj = None

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.author = self.request.user
        self.obj.save()
        return super().form_valid(form)


class UpdateNews(LoginRequiredMixin, UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_update_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.object.author != self.request.user:
            return self.handle_no_permission()
        return kwargs


class DeleteNews(LoginRequiredMixin, DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.object.author != self.request.user:
            return self.handle_no_permission()
        return kwargs
