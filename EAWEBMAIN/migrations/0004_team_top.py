# Generated by Django 5.1 on 2024-08-26 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EAWEBMAIN', '0003_group_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team_TOP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('flag_url', models.URLField()),
            ],
        ),
    ]
