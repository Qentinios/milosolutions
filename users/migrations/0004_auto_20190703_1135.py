# Generated by Django 2.2.3 on 2019-07-03 11:35

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_milouser_random'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milouser',
            name='random',
            field=models.IntegerField(default=users.models.random_int, editable=False),
        ),
    ]
