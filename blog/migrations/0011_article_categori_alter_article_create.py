# Generated by Django 4.0.3 on 2022-03-20 02:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_article_create_alter_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='categori',
            field=models.CharField(default='test', max_length=20),
        ),
        migrations.AlterField(
            model_name='article',
            name='create',
            field=models.DateField(default=datetime.datetime(2022, 3, 20, 2, 33, 32, 124585, tzinfo=utc)),
        ),
    ]
