# Generated by Django 4.2.5 on 2023-10-05 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heyderapp', '0017_rename_content_en_about_content_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='content2',
            field=models.CharField(default='', max_length=3200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='contentbig',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
