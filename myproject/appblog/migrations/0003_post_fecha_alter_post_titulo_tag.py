# Generated by Django 4.0.6 on 2022-12-08 22:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0002_post_titulo_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fecha',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo_tag',
            field=models.CharField(max_length=60),
        ),
    ]