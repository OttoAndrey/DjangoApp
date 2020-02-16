# Generated by Django 3.0.2 on 2020-02-16 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190623_2031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_pub']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, unique=True),
        ),
    ]
