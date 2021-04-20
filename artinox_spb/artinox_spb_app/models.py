from django.db import models

# Create your models here.

class PageContent(models.Model):
    block_name = models.CharField(max_length=255)
    content_text = models.TextField(blank=True)
    creation_date = models.DateField(auto_now_add=True)
    moderation_date = models.DateField(auto_now=True)
    visibility = models.BooleanField(default=True)
    page = models.ForeignKey('PageName', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.block_name

    class Meta:
        verbose_name = 'Контент страниц'
        verbose_name_plural = 'Контент страниц'

class PageName(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    page_name = models.CharField(max_length=255)

    def __str__(self):
        return self.title

# class PageBlocks(models.Model):
#     block_name = models.CharField(max_length=255)
#