# Generated by Django 3.2.8 on 2022-03-25 02:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_article_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create',
            field=models.DateField(default=datetime.datetime(2022, 3, 25, 2, 13, 13, 110897, tzinfo=utc)),
        ),
    ]
