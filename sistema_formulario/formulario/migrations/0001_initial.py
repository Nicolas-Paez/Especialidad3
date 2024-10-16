# Generated by Django 4.1.13 on 2024-10-15 15:51

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudiante_id', models.CharField(max_length=100)),
                ('respuestas', djongo.models.fields.JSONField()),
                ('nota', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=300)),
                ('es_opcion_multiple', models.BooleanField(default=False)),
                ('formulario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulario.formulario')),
            ],
        ),
    ]
