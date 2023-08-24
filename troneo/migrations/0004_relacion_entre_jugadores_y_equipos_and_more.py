# Generated by Django 4.2.4 on 2023-08-23 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('troneo', '0003_remove_jugador_suequipo_partido_clasificacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='relacion_entre_jugadores_y_equipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='troneo.equipo')),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='troneo.jugador')),
            ],
        ),
        migrations.CreateModel(
            name='relacion_entre_equipos_y_partidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='troneo.equipo')),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='troneo.partido')),
            ],
        ),
        migrations.CreateModel(
            name='relacion_entre_entrenadores_y_equipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrenador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='troneo.entrenador')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='troneo.equipo')),
            ],
        ),
    ]