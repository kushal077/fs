# Generated by Django 2.1.5 on 2019-04-16 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0002_auto_20190416_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_city', models.CharField(default='INDIA- Delhi NCR', max_length=10)),
                ('fullname', models.CharField(max_length=20)),
                ('phone_no', models.CharField(max_length=10)),
                ('street_address', models.CharField(max_length=100)),
                ('payment', models.CharField(default='COD', max_length=100)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]