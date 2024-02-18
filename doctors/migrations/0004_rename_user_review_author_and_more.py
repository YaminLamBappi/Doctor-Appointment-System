# Generated by Django 5.0.2 on 2024-02-18 13:09

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='comment',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='review',
            name='doctor',
        ),
        migrations.AddField(
            model_name='doctor',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='image_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='doctor',
            name='patient_reviews',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.review'),
        ),
        migrations.AddField(
            model_name='review',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(),
        ),
    ]