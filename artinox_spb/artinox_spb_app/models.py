from django.db import models

# Create your models here.

class PageContent(models.Model):
    title = models.CharField(max_length=255)
    block_name = models.CharField(max_length=255)
    content_text = models.TextField(blank=True)
    creation_date = models.DateField(auto_now_add=True)
    moderation_date = models.DateField(auto_now=True)
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.title
