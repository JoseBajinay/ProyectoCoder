# Generated by Django 4.0.6 on 2022-07-24 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Familiares', '0004_alter_pariente_fecha_de_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pariente',
            name='fecha_de_nacimiento',
            field=models.DateField(),
        ),
    ]
