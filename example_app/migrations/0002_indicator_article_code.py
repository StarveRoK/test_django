# Generated by Django 5.0.7 on 2024-07-26 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicator',
            name='article_code',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
