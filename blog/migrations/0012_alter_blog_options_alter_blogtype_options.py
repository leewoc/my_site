# Generated by Django 4.2.2 on 2024-06-01 18:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0011_delete_readnum"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={"ordering": ["-created_time"], "verbose_name_plural": "博客"},
        ),
        migrations.AlterModelOptions(
            name="blogtype",
            options={"verbose_name_plural": "分类"},
        ),
    ]