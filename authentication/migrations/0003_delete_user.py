# Generated by Django 4.1.7 on 2023-03-12 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0002_user"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]
