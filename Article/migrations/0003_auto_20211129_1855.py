# Generated by Django 3.2.3 on 2021-11-29 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0002_auto_20211128_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='indexpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Başlıq')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Icon')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'Index səhifəsinin məlumatları',
                'verbose_name_plural': 'İndex səhifəsinin məlumatları',
            },
        ),
        migrations.CreateModel(
            name='sosials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=150, verbose_name='Şəbəkənin adı (ingiliscə) ')),
                ('link', models.CharField(max_length=500, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Sosial şəbəkə',
                'verbose_name_plural': 'Sosial şəbəkələr',
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Paylaşım vaxtı'),
        ),
    ]
