# Generated by Django 4.2 on 2023-09-25 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heyderapp', '0013_alter_article_category_alter_photo_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
