# Generated by Django 3.2.3 on 2021-05-28 16:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20210528_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(blank=True, max_length=20, verbose_name='작성자'),
        ),
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, max_length=10, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(blank=True, max_length=20, verbose_name='작성자 / Writer'),
        ),
        migrations.AlterField(
            model_name='post',
            name='contents',
            field=models.TextField(blank=True, max_length=1000, verbose_name='내용 / Contents'),
        ),
    ]