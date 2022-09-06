# Generated by Django 4.1 on 2022-09-06 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_aboutus_delete_googlemaps'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutus2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='Aboutus image')),
                ('title', models.CharField(max_length=40, verbose_name='Aboutus title')),
                ('text2', models.TextField(verbose_name='Aboutus text2')),
                ('urlabout', models.URLField(verbose_name='Aboutus url')),
                ('details', models.TextField(verbose_name='Aboutus about')),
            ],
            options={
                'verbose_name': 'Aboutus2',
                'verbose_name_plural': 'Aboutuss2',
            },
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='urlabout',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='details',
            field=models.TextField(default=1, verbose_name='Aboutus about'),
            preserve_default=False,
        ),
    ]
