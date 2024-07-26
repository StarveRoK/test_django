# Generated by Django 5.0.7 on 2024-07-26 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_app', '0002_indicator_article_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicatorLineHeaderView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_valid_until', models.DateField()),
                ('article_name', models.CharField(max_length=255)),
                ('article_code', models.CharField(max_length=255)),
                ('order', models.PositiveIntegerField()),
                ('last_updated_indicator', models.DateTimeField()),
                ('updated_by_indicator', models.CharField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('organization', models.CharField()),
                ('created_at', models.DateTimeField()),
                ('distribution_count', models.IntegerField()),
                ('targeted_distribution_count', models.IntegerField()),
                ('last_updated_line', models.DateTimeField()),
                ('updated_by_line', models.CharField()),
            ],
            options={
                'db_table': 'indicator_line_view',
                'managed': False,
            },
        ),
    ]
