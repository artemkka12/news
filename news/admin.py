from django.contrib import admin
from .models import News, Category


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


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
