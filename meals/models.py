from django.db import models

class Recipe(models.Model):
    slug = models.SlugField(unique=True)
    article_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=48)
    description = models.TextField(blank=True)
    article = models.TextField(blank=True)
    ingredients = models.JSONField(default=list, blank=True)
    procedure = models.JSONField(default=list, blank=True)
    images = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.short_name
