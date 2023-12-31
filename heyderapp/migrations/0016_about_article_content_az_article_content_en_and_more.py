# Generated by Django 4.2.5 on 2023-10-04 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heyderapp', '0015_article_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minititle', models.CharField(max_length=100)),
                ('minititle_az', models.CharField(max_length=100, null=True)),
                ('minititle_en', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=180)),
                ('title_az', models.CharField(max_length=180, null=True)),
                ('title_en', models.CharField(max_length=180, null=True)),
                ('content', models.CharField(max_length=3200)),
                ('content_az', models.CharField(max_length=3200, null=True)),
                ('content_en', models.CharField(max_length=3200, null=True)),
                ('image', models.ImageField(upload_to='', verbose_name='690-732')),
                ('imza', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='content_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='name_az',
            field=models.CharField(max_length=1200, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='name_en',
            field=models.CharField(max_length=1200, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='bottomcontent_az',
            field=models.CharField(blank=True, max_length=12000, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='bottomcontent_en',
            field=models.CharField(blank=True, max_length=12000, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='bottomname_az',
            field=models.CharField(blank=True, max_length=1200, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='bottomname_en',
            field=models.CharField(blank=True, max_length=1200, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_without_ck_az',
            field=models.CharField(blank=True, max_length=1200, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_without_ck_en',
            field=models.CharField(blank=True, max_length=1200, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='name_az',
            field=models.CharField(max_length=1200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='name_en',
            field=models.CharField(max_length=1200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='sidecontent_az',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='sidecontent_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='sidename_az',
            field=models.CharField(blank=True, max_length=230, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='sidename_en',
            field=models.CharField(blank=True, max_length=230, null=True),
        ),
        migrations.AddField(
            model_name='homeheader',
            name='content_az',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homeheader',
            name='content_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homeheader',
            name='title_az',
            field=models.CharField(blank=True, max_length=1200, null=True),
        ),
        migrations.AddField(
            model_name='homeheader',
            name='title_en',
            field=models.CharField(blank=True, max_length=1200, null=True),
        ),
        migrations.AddField(
            model_name='homeheadervideo',
            name='name_az',
            field=models.CharField(max_length=230, null=True),
        ),
        migrations.AddField(
            model_name='homeheadervideo',
            name='name_en',
            field=models.CharField(max_length=230, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='content_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='name_az',
            field=models.CharField(max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='name_en',
            field=models.CharField(max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='content_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='name_az',
            field=models.CharField(max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='name_en',
            field=models.CharField(max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='content_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='name_az',
            field=models.CharField(max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='name_en',
            field=models.CharField(max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='homeheadervideo',
            name='video',
            field=models.CharField(default=2, max_length=3400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.CharField(max_length=3400),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.CharField(max_length=3200),
        ),
    ]
