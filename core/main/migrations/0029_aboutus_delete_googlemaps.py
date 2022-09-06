# Generated by Django 4.1 on 2022-09-06 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_googlemaps'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='Aboutus image')),
                ('title', models.CharField(max_length=40, verbose_name='Aboutus title')),
                ('text1', models.TextField(verbose_name='Aboutus text1')),
                ('text2', models.TextField(verbose_name='Aboutus text2')),
                ('urlabout', models.URLField(verbose_name='Aboutus url')),
            ],
            options={
                'verbose_name': 'Aboutus',
                'verbose_name_plural': 'Aboutuss',
            },
        ),
        migrations.DeleteModel(
            name='Googlemaps',
        ),
    ]