# Generated by Django 4.1 on 2022-08-30 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_category_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Callus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media', verbose_name='Product image')),
                ('title', models.CharField(max_length=30, verbose_name='Product name')),
                ('tell', models.CharField(max_length=30, verbose_name='Tell number')),
            ],
            options={
                'verbose_name': 'Callus',
                'verbose_name_plural': 'Callus',
            },
        ),
    ]