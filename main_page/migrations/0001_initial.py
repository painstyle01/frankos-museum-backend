# Generated by Django 4.0.3 on 2022-04-21 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backgrounds', models.FileField(upload_to='backgrounds/')),
            ],
        ),
    ]