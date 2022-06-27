# Generated by Django 4.0.4 on 2022-06-27 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventasgamer', '0008_contacto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='periferico',
            name='idperiferico',
        ),
        migrations.RemoveField(
            model_name='periferico',
            name='marca',
        ),
        migrations.RemoveField(
            model_name='periferico',
            name='modelo',
        ),
        migrations.AddField(
            model_name='periferico',
            name='descripcion',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='periferico',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
        migrations.AlterField(
            model_name='periferico',
            name='nombre',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='periferico',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
