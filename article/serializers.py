from rest_framework import serializers
from .models import Article
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    # author = serializers.CharField(source='author.username', read_only=True)
    author_id = serializers.IntegerField(write_only=True)

    class Meta:
        model=Article
        fields=('title','author','content', 'author_id')
        depth = 1
