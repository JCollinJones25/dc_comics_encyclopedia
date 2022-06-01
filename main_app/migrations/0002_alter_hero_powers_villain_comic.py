# Generated by Django 4.0.4 on 2022-06-01 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='powers',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('heroes', models.ManyToManyField(to='main_app.hero')),
            ],
        ),
    ]