# Generated by Django 3.2.8 on 2022-03-25 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='darkhast',
            name='how_to_send',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
