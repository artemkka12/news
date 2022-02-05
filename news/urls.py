from django.urls import path
from django.conf.urls.static import static
from mysite import settings
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('', views.HomeNews.as_view(), name='index'),
    path('categories/', views.Categories.as_view(), name='categories'),
    path('authors/', views.Authors.as_view(), name='authors'),
    path('category/<int:category_id>', views.NewsByCategory.as_view(), name='category'),
    path('author/<int:author_id>', views.NewsByAuthor.as_view(), name='author'),
    path('news/add-news', views.CreateNews.as_view(), name='add-news'),
    path('news/<int:pk>', views.ViewNews.as_view(), name='view-news'),
    path('news/update-news/<int:pk>', views.UpdateNews.as_view(), name='update-news'),
    path('news/delete-news/<int:pk>', views.DeleteNews.as_view(), name='delete-news'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


