# Generated by Django 4.1 on 2022-08-30 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_dishes_slug_alter_dishes_index_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes',
            name='price',
            field=models.IntegerField(),
        ),
    ]
