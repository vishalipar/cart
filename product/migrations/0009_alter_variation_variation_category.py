# Generated by Django 5.1.4 on 2024-12-21 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0008_alter_variation_variation_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="variation",
            name="variation_category",
            field=models.CharField(
                choices=[("color", "color"), ("size", "size")], max_length=100
            ),
        ),
    ]
