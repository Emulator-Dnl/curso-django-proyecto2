# Generated by Django 4.2.5 on 2023-09-12 22:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_options_alter_post_categories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 12, 22, 8, 22, 436733, tzinfo=datetime.timezone.utc), verbose_name='Fecha de publicación'),
        ),
    ]