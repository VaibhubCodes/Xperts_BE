# Generated by Django 5.1.1 on 2024-10-03 19:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohorts', '0104_alter_cohort_end_date_alter_cohort_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cohort',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 2, 19, 20, 47, 16883, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='cohort',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 2, 19, 20, 47, 16626, tzinfo=datetime.timezone.utc)),
        ),
    ]
