# Generated by Django 5.0 on 2024-06-18 20:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('industry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('work_description', models.TextField()),
                ('date_started', models.DateField()),
                ('date_ended', models.DateField(blank=True, null=True)),
                ('currently_working', models.BooleanField(default=False)),
                ('industry_expertise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_experiences', to='industry.expertise')),
            ],
        ),
    ]
