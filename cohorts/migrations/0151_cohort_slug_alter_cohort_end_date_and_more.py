# Generated by Django 5.1.1 on 2024-11-17 10:24

import datetime
from django.db import migrations, models
from django.utils.text import slugify


def populate_cohort_slugs(apps, schema_editor):
    Cohort = apps.get_model('cohorts', 'Cohort')
    for cohort in Cohort.objects.all():
        base_slug = slugify(cohort.name)
        slug = base_slug
        counter = 1
        while Cohort.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        cohort.slug = slug
        cohort.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cohorts', '0150_alter_cohort_end_date_alter_cohort_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cohort',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='cohort',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 17, 10, 24, 4, 94010, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='cohort',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 17, 10, 24, 4, 93746, tzinfo=datetime.timezone.utc)),
        ),
        migrations.RunPython(populate_cohort_slugs),  # Populate unique slugs
    ]
