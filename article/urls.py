from django.contrib import admin
from django.urls import path
from . import views
from article.views import ArticleListView,NotCreate,NotUpdate,NotDetail,NotDelete,article_api,ArticleAPIView,article_detail
app_name="article"

urlpatterns = [
    path('create/', views.index,name="index"),
    path('view_notes/',ArticleListView.as_view(),name="notes"),
    path('add_notes/',NotCreate.as_view()),
    path('update_note/<int:pk>/',NotUpdate.as_view()),
    path('delete_note/<int:pk>/',NotDelete.as_view()),
    path('article/<int:pk>/',NotDetail.as_view()),
    path('article_detail/<int:pk>/',article_detail),
    path('article_api/',ArticleAPIView.as_view()),
]
