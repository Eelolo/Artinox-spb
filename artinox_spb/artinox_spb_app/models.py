from django.db import models
import os
# Create your models here.

class Page(models.Model):
    page_name = models.CharField(max_length=255, verbose_name='название страницы')


    class Meta:
        verbose_name = 'Страницы'
        verbose_name_plural = 'Страницы'
        ordering = ['id']

class PageContent(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='заголовок')
    content_text = models.TextField(blank=True, null=True, verbose_name='содержимое блока')
    photo = models.ImageField(upload_to=f'photos/{Page.page_name}', null=True, verbose_name='путь до фото')
    creation_date = models.DateField(auto_now_add=True, verbose_name='дата создания')
    moderation_date = models.DateField(auto_now=True, verbose_name='дата редактирования')
    visibility = models.BooleanField(default=True, verbose_name='видимость')
    block_name = models.CharField(max_length=255, verbose_name='название блока')
    page = models.ForeignKey('Page', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.block_name

    class Meta:
        verbose_name = 'Контент страниц'
        verbose_name_plural = 'Контент страниц'


class UsersContacts(models.Model):
    fullname = models.CharField(max_length=255, null=False, verbose_name='ФИО')
    email = models.CharField(max_length=255, null=False, verbose_name='Email')
    tel = models.CharField(max_length=16, null=False, verbose_name='Номер телефона')
    address = models.TextField(null=False, verbose_name='Адрес установки')
    product_name = models.CharField(max_length=255, null=False, verbose_name='Наименование изделия')
    task_text = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    send_date = models.DateField(auto_now_add=True, verbose_name='дата отправки')
    technical_task = models.FileField(blank=False, null=False, upload_to=f'documents/{fullname}/{product_name}/Техническое задание/')
    technical_plan = models.FileField(blank=False, null=False, upload_to=f'documents/{fullname}/{product_name}/Чертеж')
