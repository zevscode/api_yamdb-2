# Generated by Django 2.2.6 on 2021-07-16 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='titles',
            name='rating',
            field=models.IntegerField(blank=True, null=True, verbose_name='Рейтинг'),
        ),
    ]
