# Generated by Django 4.0.3 on 2022-03-07 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canvas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canvas',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
