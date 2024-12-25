# Generated by Django 5.1.4 on 2024-12-25 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0014_alter_variation_variation_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductGallery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(max_length=255, upload_to="store/products"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "productgallery",
                "verbose_name_plural": "productgallery",
            },
        ),
    ]