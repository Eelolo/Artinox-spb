from django.db import models

# Create your models here.

class PageInfo(models.Model):
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
    photo = models.ImageField(upload_to=f'photos/{PageInfo.page_name}', null=True, verbose_name='путь до фото')
    creation_date = models.DateField(auto_now_add=True, verbose_name='дата создания')
    moderation_date = models.DateField(auto_now=True, verbose_name='дата редактирования')
    visibility = models.BooleanField(default=True, verbose_name='видимость')
    block_name = models.CharField(max_length=255, verbose_name='название блока')
    page = models.ForeignKey('PageInfo', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.block_name

    class Meta:
        verbose_name = 'Контент страниц'
        verbose_name_plural = 'Контент страниц'


class UsersContacts(models.Model):
    full_name = models.TextField(blank=True, null=False, verbose_name='ФИО')
    email = models.CharField(max_length=255, verbose_name='email')
    phone = models.CharField(null=False, max_length=16, verbose_name='номер телефона')
    address = models.TextField(blank=True, null=True, verbose_name='Адрес заказчика')
    product_name = models.TextField(blank=True, null=True, verbose_name='Наименование изделия')
    #TODO: придумать хранение файлов заказчика ( тз и чертеж)
    # technical_task = models.
    #technical_plan = models.
    task_text = models.TextField(blank=True, null=True, verbose_name='Комментарий заказчика')


