# Generated by Django 3.2.7 on 2021-10-01 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_auto_20211001_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
