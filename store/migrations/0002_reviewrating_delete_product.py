# Generated by Django 5.1.4 on 2024-12-23 18:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_account_phone_number"),
        ("product", "0011_alter_variation_variation_category"),
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReviewRating",
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
                ("subject", models.CharField(blank=True, max_length=50)),
                ("review", models.TextField(blank=True, max_length=500)),
                ("rating", models.FloatField()),
                ("ip", models.CharField(blank=True, max_length=20)),
                ("status", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.account",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Product",
        ),
    ]
