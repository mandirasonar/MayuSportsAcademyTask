# Generated by Django 3.2.9 on 2024-09-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20240928_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='age',
            field=models.CharField(max_length=100),
        ),
    ]
