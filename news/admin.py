from django.contrib import admin
from .models import News, Category, Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'title',
                    'category',
                    'views',
                    'created_at',
                    'updated_at',
                    'is_published',
                    ]

    list_display_links = ['title',
                          ]

    search_fields = ['id',
                     'title',
                     ]

    list_filter = ['is_published',
                   'category',
                   ]
    list_editable = ['category',
                     'is_published',
                     ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'title',
                    ]

    list_display_links = ['title',
                          ]

    search_fields = ['title',
                     ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'comment',
                    'author',
                    'news',
                    'created_at',
                    ]

    list_display_links = ['comment',
                          ]

    search_fields = ['comment',
                     'news',
                     'author',
                     ]


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
