# Generated by Django 5.1.4 on 2024-12-24 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0004_alter_reviewrating_rating"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ReviewRating",
        ),
    ]
