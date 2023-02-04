# Generated by Django 3.2.3 on 2021-11-28 19:44

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(max_length=150, verbose_name='Kateqoriya')),
            ],
            options={
                'verbose_name': 'Subkateqoriya',
                'verbose_name_plural': 'Subkateqoriyalar',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=150, verbose_name='Subkateqoriya')),
                ('subcategory', models.ManyToManyField(blank=True, related_name='subcategories', to='Article.Subcategory', verbose_name='Kateqoriya')),
            ],
            options={
                'verbose_name': 'Kateqoriya',
                'verbose_name_plural': 'Kateqoriyalar',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Başlıq')),
                ('subtitle', models.CharField(max_length=150, verbose_name='Altbaşlıq')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Şəkil')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Məzmun')),
                ('like', models.IntegerField(default=0, verbose_name='Like')),
                ('view', models.IntegerField(default=0, verbose_name='Baxış sayı')),
                ('comment_count', models.CharField(default='0', max_length=150, verbose_name='Kommentsayı')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(blank=True, to='Article.Category', verbose_name='Kateqoriya')),
                ('subcategory', models.ManyToManyField(blank=True, to='Article.Subcategory', verbose_name='Subkateqoriya')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Postlar',
                'ordering': ['-created_date'],
            },
        ),
    ]