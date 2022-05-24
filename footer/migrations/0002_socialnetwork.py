# Generated by Django 4.0.3 on 2022-05-18 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("footer", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SocialNetwork",
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
                ("name", models.CharField(max_length=200)),
                ("link", models.URLField()),
                ("logo", models.FileField(upload_to="social_network/")),
            ],
        ),
    ]
