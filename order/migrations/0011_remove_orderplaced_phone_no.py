# Generated by Django 2.2 on 2019-04-16 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20190416_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='phone_no',
        ),
    ]
