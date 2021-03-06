# Generated by Django 3.2.5 on 2021-08-01 03:21

from django.db import migrations, models
import django.db.models.deletion
import homepage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=15, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('stock', models.PositiveSmallIntegerField(default=0)),
                ('description', models.TextField(max_length=100)),
                ('img_url', models.ImageField(blank=True, null=True, upload_to=homepage.models.get_image_path)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.category')),
            ],
        ),
    ]
