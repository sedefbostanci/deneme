from django.contrib import admin
from .models import Article
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=["title","author","content","created_date"]
    search_fields=["title"]
    class Meta:
        model=Article
# Register your models here.
