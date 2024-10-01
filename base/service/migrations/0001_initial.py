# Generated by Django 5.1.1 on 2024-09-26 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='titulo')),
                ('content', models.TextField(max_length=200, verbose_name='contenido')),
                ('image', models.ImageField(upload_to='', verbose_name='imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creada')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='actualizada')),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'servicios',
            },
        ),
    ]
