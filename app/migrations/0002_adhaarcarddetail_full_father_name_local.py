# Generated by Django 5.0.6 on 2024-05-27 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adhaarcarddetail',
            name='full_father_name_local',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
