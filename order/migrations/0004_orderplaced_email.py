# Generated by Django 2.1.5 on 2019-04-16 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_orderplaced'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplaced',
            name='email',
            field=models.EmailField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]