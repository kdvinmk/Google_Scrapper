# Generated by Django 3.0.4 on 2020-03-29 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0002_auto_20200329_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
    ]
