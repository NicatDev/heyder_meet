# Generated by Django 4.2.5 on 2023-10-05 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heyderapp', '0018_about_content2_about_contentbig'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='content2_az',
            field=models.CharField(max_length=3200, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='content2_ru',
            field=models.CharField(max_length=3200, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='contentbig_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='contentbig_ru',
            field=models.TextField(null=True),
        ),
    ]
