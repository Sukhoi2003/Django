# Generated by Django 4.2.5 on 2023-09-09 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
