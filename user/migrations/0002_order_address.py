# Generated by Django 5.1.2 on 2024-12-24 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='No address', max_length=255),
        ),
    ]