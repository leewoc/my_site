# Generated by Django 4.2.2 on 2024-05-27 09:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_rename_created_blog_created_time_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={"ordering": ["-created_time"]},
        ),
    ]
