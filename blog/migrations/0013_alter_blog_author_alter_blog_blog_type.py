# Generated by Django 4.2.2 on 2024-06-07 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0012_alter_blog_options_alter_blogtype_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="blog",
            name="blog_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="blog_blog",
                to="blog.blogtype",
            ),
        ),
    ]
