# Generated by Django 4.2.2 on 2024-06-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_profile_avatar_profile_bio_profile_phone_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="nickname",
            field=models.CharField(blank=True, max_length=20, verbose_name="昵称"),
        ),
    ]
