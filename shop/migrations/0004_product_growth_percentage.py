# Generated by Django 5.1.3 on 2024-12-04 20:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0003_product_max_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="growth_percentage",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
