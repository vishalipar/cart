# Generated by Django 5.1.4 on 2024-12-24 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0011_alter_variation_variation_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="variation",
            name="variation_category",
            field=models.CharField(
                choices=[("size", "size"), ("color", "color")], max_length=100
            ),
        ),
    ]
