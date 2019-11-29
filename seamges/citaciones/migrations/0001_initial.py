# Generated by Django 2.2.7 on 2019-11-29 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profesionales', '0001_initial'),
        ('prestaciones', '0001_initial'),
        ('casos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_agenda', models.DateTimeField(verbose_name='Fecha en Agenda')),
                ('observacion', models.TextField(verbose_name='Observación Citación')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('caso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casos.Caso')),
                ('prestacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestaciones.Prestacion')),
                ('profesional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesionales.Profesional')),
            ],
            options={
                'verbose_name': 'Citación',
                'verbose_name_plural': 'Citaciones',
                'ordering': ['-fecha_agenda'],
            },
        ),
    ]
