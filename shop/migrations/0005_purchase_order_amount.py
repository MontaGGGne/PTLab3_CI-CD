# Generated by Django 5.1.3 on 2024-12-04 20:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0004_product_growth_percentage"),
    ]

    operations = [
        migrations.AddField(
            model_name="purchase",
            name="order_amount",
            field=models.PositiveIntegerField(default=0),
        ),
    ]