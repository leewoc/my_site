# Generated by Django 4.2.2 on 2024-06-05 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("comment", "0002_alter_comment_options_comment_parent_id_reply"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="parent_id",
        ),
        migrations.AddField(
            model_name="comment",
            name="parent",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="comment.comment",
            ),
        ),
        migrations.DeleteModel(
            name="Reply",
        ),
    ]
