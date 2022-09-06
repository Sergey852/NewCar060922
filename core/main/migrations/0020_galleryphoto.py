# Generated by Django 4.1 on 2022-09-03 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_services_second_column_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galleryphoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='Galleryphoto image')),
                ('modclass', models.CharField(max_length=30, verbose_name='Galleryphoto class')),
                ('imgpng', models.ImageField(upload_to='media', verbose_name='png image')),
            ],
            options={
                'verbose_name': 'Galleryphoto',
                'verbose_name_plural': 'Galleryphotos',
            },
        ),
    ]
