# Generated by Django 4.1 on 2022-09-03 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_customer_services_alter_car_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer_services',
            old_name='tilte',
            new_name='title',
        ),
    ]