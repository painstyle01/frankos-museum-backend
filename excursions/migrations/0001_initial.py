# Generated by Django 4.0.3 on 2022-06-07 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Excursion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excursion', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
    ]
