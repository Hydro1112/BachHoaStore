# Generated by Django 5.1.2 on 2025-01-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_holiday_product_holiday_promotion_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewrating',
            name='flagged_as_spam',
            field=models.BooleanField(default=False),
        ),
    ]
