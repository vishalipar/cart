# Generated by Django 5.1.4 on 2024-12-26 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0015_productgallery"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productgallery",
            options={
                "verbose_name": "product gallery",
                "verbose_name_plural": "product gallery",
            },
        ),
    ]