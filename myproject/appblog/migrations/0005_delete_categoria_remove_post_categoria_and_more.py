# Generated by Django 4.0.6 on 2022-12-09 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0004_categoria_post_categoria'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.RemoveField(
            model_name='post',
            name='categoria',
        ),
        migrations.AddField(
            model_name='post',
            name='descripcion',
            field=models.CharField(default='codigo', max_length=100),
        ),
    ]