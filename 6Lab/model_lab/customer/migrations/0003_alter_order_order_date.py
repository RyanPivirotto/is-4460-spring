# Generated by Django 5.0.1 on 2024-02-28 21:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_email_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
