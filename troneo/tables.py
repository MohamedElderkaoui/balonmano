import django_tables2 as tables
from .models import jugador, entrenador, Equipo, Partido, clasificacion, relacion_entre_jugadores_y_equipos, relacion_entre_entrenadores_y_equipos, relacion_entre_equipos_y_partidos

class JugadorTable(tables.Table):
    #     add td action left table detail, edit, delete from table
    action = tables.TemplateColumn(
        
        '<a href="{% url \'jugadores:jugador-detail\' record.pk %}"><button type="button" class="btn btn-primary">Detail</button></a> <a href="{% url \'jugadores:jugador-update\' record.pk %}"><button type="button" class="btn btn-warning">Edit</button></a> <a href="{% url \'jugadores:jugador-delete\' record.pk %}"><button type="button" class="btn btn-danger">Delete</button></a>',
        verbose_name='Actions')
    class Meta:
        model = jugador
        template_name = 'django_tables2/bootstrap4.html'  # Use Bootstrap styling
        fields = ('nombre', 'apellido', 'edad', 'posicion', 'nacionalidad', 'foto', 'action')

class entrenadorTable(tables.Table):
    #     add td action left table detail, edit, delete from table
    action = tables.TemplateColumn(
        
        '<a href="{% url \'jugadores:entrenador-detail\' record.pk %}"><button type="button" class="btn btn-primary">Detail</button></a> <a href="{% url \'jugadores:entrenador-update\' record.pk %}"><button type="button" class="btn btn-warning">Edit</button></a> <a href="{% url \'jugadores:entrenador-delete\' record.pk %}"><button type="button" class="btn btn-danger">Delete</button></a>',
        verbose_name='Actions')
    class Meta:
        model = entrenador
        template_name = 'django_tables2/bootstrap4.html'  # Use Bootstrap styling
        fields = ('nombre', 'apellido', 'edad', 'nacionalidad', 'foto', 'action')