# Generated by Django 3.2 on 2021-05-27 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=255, verbose_name='название страницы')),
            ],
            options={
                'verbose_name': 'Страницы',
                'verbose_name_plural': 'Страницы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='UsersContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, verbose_name='ФИО')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('tel', models.CharField(max_length=16, verbose_name='Номер телефона')),
                ('address', models.TextField(verbose_name='Адрес установки')),
                ('product_name', models.CharField(max_length=255, verbose_name='Наименование изделия')),
                ('task_text', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('send_date', models.DateField(auto_now_add=True, verbose_name='дата отправки')),
                ('technical_task', models.FileField(upload_to='documents/<django.db.models.fields.CharField>/<django.db.models.fields.CharField>/Техническое задание/')),
                ('technical_plan', models.FileField(upload_to='documents/<django.db.models.fields.CharField>/<django.db.models.fields.CharField>/Чертеж')),
            ],
        ),
        migrations.CreateModel(
            name='PageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='заголовок')),
                ('content_text', models.TextField(blank=True, null=True, verbose_name='содержимое блока')),
                ('photo', models.ImageField(null=True, upload_to='photos/<django.db.models.query_utils.DeferredAttribute object at 0x0000021CBDC997C0>', verbose_name='путь до фото')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('moderation_date', models.DateField(auto_now=True, verbose_name='дата редактирования')),
                ('visibility', models.BooleanField(default=True, verbose_name='видимость')),
                ('block_name', models.CharField(max_length=255, verbose_name='название блока')),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='artinox_spb_app.page')),
            ],
            options={
                'verbose_name': 'Контент страниц',
                'verbose_name_plural': 'Контент страниц',
            },
        ),
    ]
