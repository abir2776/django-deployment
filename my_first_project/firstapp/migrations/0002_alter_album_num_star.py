# Generated by Django 3.2.11 on 2022-02-06 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='num_star',
            field=models.IntegerField(choices=[(1, 'Bad'), (2, 'Not Bad'), (3, 'Average'), (4, 'Good'), (5, 'Excellent')]),
        ),
    ]
