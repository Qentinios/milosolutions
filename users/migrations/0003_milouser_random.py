# Generated by Django 2.2.3 on 2019-07-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_milouser_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='milouser',
            name='random',
            field=models.IntegerField(default=17, editable=False),
        ),
    ]