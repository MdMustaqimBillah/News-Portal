# Generated by Django 5.1 on 2024-08-26 04:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(upload_to='advertisement')),
                ('link', models.URLField(blank=True, null=True)),
                ('clicks', models.IntegerField(default=0)),
                ('content', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('validity', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='NewsApp/')),
                ('views', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('politics', 'Politics'), ('sports', 'Sports'), ('entertainment', 'Entertainment'), ('finance', 'Finance'), ('international', 'International'), ('social', 'Social'), ('nature', 'Nature'), ('science', 'Science'), ('tech', 'Tech'), ('national', 'National'), ('life style', 'LifeStyle'), ('trending', 'Trending')], default='world', max_length=20)),
                ('importance_level', models.CharField(choices=[('main', 'Main'), ('r2c1', 'Row 2 Column 1'), ('r2c2', 'Row 2 Column 2'), ('r2c3', 'Row 2 Column 3'), ('r3c1', 'Row 3 Column 1'), ('r3c2', 'Row 3 Column 2'), ('r3c3', 'Row 3 Column 3'), ('r4c1', 'Row 4 Column 1'), ('r4c2', 'Row 4 Column 2'), ('r4c3', 'Row 4 Column 3'), ('r4c4', 'Row 4 Column 4'), ('r5c1', 'Row 5 Column 1'), ('r5c2', 'Row 5 Column 2'), ('r5c3', 'Row 5 Column 3'), ('r5c4', 'Row 5 Column 4')], default='main', max_length=20)),
                ('article_ad', models.ImageField(blank=True, null=True, upload_to='article_ad')),
                ('company', models.TextField(blank=True, null=True)),
                ('link_ad', models.URLField(blank=True, null=True)),
                ('description_ad', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]