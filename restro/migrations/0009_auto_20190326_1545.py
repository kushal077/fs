# Generated by Django 2.1.5 on 2019-03-26 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restro', '0008_auto_20190316_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='cuisines',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='cuisines',
            field=models.CharField(choices=[('American', 'american'), ('Thai', 'thai'), ('Mexican', 'mexican'), ('chinese', 'Chinese'), ('indian', 'indian'), ('Desert', 'Desert')], default=1, max_length=2),
            preserve_default=False,
        ),
    ]
