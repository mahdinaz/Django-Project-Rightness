# Generated by Django 4.0.3 on 2022-03-18 00:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 18, 0, 40, 22, 649289, tzinfo=utc)),
        ),
    ]