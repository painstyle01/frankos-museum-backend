# Generated by Django 4.0.3 on 2022-04-21 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.TextField()),
                ('source_name', models.TextField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('book', 'Книжка'), ('statue', 'Фігурка'), ('trinket', 'Брелок')], default='book', max_length=25),
        ),
    ]