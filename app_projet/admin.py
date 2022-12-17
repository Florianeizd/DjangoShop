from django.contrib import admin

from .models import Article
from .models import Order
from .models import Cart

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','article_name', 'image', 'stock', 'price')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Order)
admin.site.register(Cart)
