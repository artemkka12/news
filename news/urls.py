from django.urls import path
from django.conf.urls.static import static
from mysite import settings
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('', views.HomeNews.as_view(), name='index'),
    path('category/<int:category_id>', views.NewsByCategory.as_view(extra_context={'title': 'Страница'}), name='category'),
    path('news/<int:pk>', views.ViewNews.as_view(), name='view-news'),
    path('news/add-news', views.CreateNews.as_view(), name='add-news'),
    path('news/update-news/<int:pk>', views.UpdateNews.as_view(), name='update-news'),
    path('news/delete-news/<int:pk>', views.DeleteNews.as_view(), name='delete-news'),
]



