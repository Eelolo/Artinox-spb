from django.db import models

# Create your models here.

class PageName(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='заголовок')
    page_name = models.CharField(max_length=255, verbose_name='название страницы')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страницы'
        verbose_name_plural = 'Страницы'
        ordering = ['id']

class PageContent(models.Model):
    content_text = models.TextField(blank=True, null=True, verbose_name='содержимое блока')
    photo = models.ImageField(upload_to=f'photos/{PageName.page_name}', null=True, verbose_name='путь до фото')
    creation_date = models.DateField(auto_now_add=True, verbose_name='дата создания')
    moderation_date = models.DateField(auto_now=True, verbose_name='дата редактирования')
    visibility = models.BooleanField(default=True, verbose_name='видимость')
    block_name = models.CharField(max_length=255, verbose_name='название блока')
    page = models.ForeignKey('PageName', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.block_name

    class Meta:
        verbose_name = 'Контент страниц'
        verbose_name_plural = 'Контент страниц'


