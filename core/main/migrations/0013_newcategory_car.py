# Generated by Django 4.1 on 2022-09-01 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_carmodel_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media', verbose_name='Category image')),
                ('title', models.CharField(max_length=30, verbose_name='Category name')),
            ],
            options={
                'verbose_name': 'Newcategory',
                'verbose_name_plural': 'Newcategorys',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media', verbose_name='Car image')),
                ('title', models.TextField(verbose_name='Car about')),
                ('price', models.CharField(max_length=30, verbose_name='Car price')),
                ('imgpng', models.ImageField(upload_to='media', verbose_name='ADD image')),
                ('category', models.ManyToManyField(to='main.newcategory')),
            ],
        ),
    ]
