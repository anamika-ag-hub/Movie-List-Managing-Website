# Generated by Django 5.1.4 on 2025-01-15 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0002_delete_movieinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('year', models.IntegerField(null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
