# Generated by Django 3.1.4 on 2021-01-12 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210112_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawalrequest',
            name='desc',
            field=models.TextField(blank=True, verbose_name='Description '),
        ),
    ]
