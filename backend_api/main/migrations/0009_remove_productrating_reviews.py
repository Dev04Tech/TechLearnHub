# Generated by Django 5.0.7 on 2024-07-20 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_review_productrating_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productrating',
            name='reviews',
        ),
    ]