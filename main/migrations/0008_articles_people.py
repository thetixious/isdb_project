# Generated by Django 4.2.8 on 2023-12-26 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_articles'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='people',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.people'),
        ),
    ]
