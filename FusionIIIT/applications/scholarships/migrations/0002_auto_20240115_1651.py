# Generated by Django 3.1.5 on 2024-01-15 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='previous_winner',
            name='year',
            field=models.IntegerField(default=2024),
        ),
    ]
