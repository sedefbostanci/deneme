from django.db import models
from django.urls import reverse
# Create your models here.
class Article(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,blank=True, null=True)
    title=models.CharField(max_length=50)
    content=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("index")
    def __str__(self):
        return self.title
