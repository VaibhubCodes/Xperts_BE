# Generated by Django 5.1.1 on 2024-11-17 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohorts', '0151_cohort_slug_alter_cohort_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cohort',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 17, 10, 26, 2, 800350, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='cohort',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 17, 10, 26, 2, 800134, tzinfo=datetime.timezone.utc)),
        ),
    ]
