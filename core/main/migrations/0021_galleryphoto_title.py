# Generated by Django 4.1 on 2022-09-03 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_galleryphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryphoto',
            name='title',
            field=models.CharField(default=1, max_length=30, verbose_name='Galleryphoto title'),
            preserve_default=False,
        ),
    ]