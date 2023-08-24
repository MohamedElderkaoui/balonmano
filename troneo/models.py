from django.db import models
# Create your models here.

# class jugador(models.Model):
class jugador(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField(default=19)
    posicion = models.CharField(max_length=20)
    nacionalidad = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)
    def __str__(self):
        return self.nombre
   

class entrenador(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField(default=19)
    nacionalidad = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)
    def __str__(self):
        return self.nombre
class Equipo(models.Model):
    nombre = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    entrenador = models.ForeignKey(entrenador, on_delete=models.CASCADE)
    # un jugador puede estar en un solo equipo
    # un equipo puede tener muchos jugadores
    
    puntos = models.IntegerField(default=0)
    partidos_jugados = models.IntegerField(default=0)
    partidos_ganados = models.IntegerField(default=0)
    partidos_empatados = models.IntegerField(default=0)
    partidos_perdidos = models.IntegerField(default=0)
    goles_favor = models.IntegerField(default=0)
    goles_contra = models.IntegerField(default=0)
    jugadores = models.ManyToManyField(jugador)
    def __str__(self):
        return self.nombre
    
 # alter table jugador add column equipo_id integer references equipo(id);
#  equipo_v
class Partido(models.Model):
    fecha = models.DateField()
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='local')
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='visitante',
                                         limit_choices_to={'id__ne': models.F('equipo_local')})
    goles_local = models.IntegerField(default=0)
    goles_visitante = models.IntegerField(default=0)
    def __str__(self):
        return self.equipo_local.nombre + ' - ' + self.equipo_visitante.nombre
    # excuiendo el equipo local en las opciones del visitante
class clasificacion(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    puntos = models.IntegerField(default=0)
    partidos_jugados = models.IntegerField(default=0)
    partidos_ganados = models.IntegerField(default=0)
    partidos_empatados = models.IntegerField(default=0)
    partidos_perdidos = models.IntegerField(default=0)
    goles_favor = models.IntegerField(default=0)
    goles_contra = models.IntegerField(default=0)
    def __str__(self):
        return self.equipo.nombre
    
class relacion_entre_jugadores_y_equipos(models.Model):
    jugador = models.ForeignKey(jugador, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    def __str__(self):
        return self.jugador.nombre + ' - ' + self.equipo.nombre
class relacion_entre_entrenadores_y_equipos(models.Model):
    entrenador = models.ForeignKey(entrenador, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    def __str__(self):
        return self.entrenador.nombre + ' - ' + self.equipo.nombre
class relacion_entre_equipos_y_partidos(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    def __str__(self):
        return self.equipo.nombre + ' - ' + self.partido.equipo_local.nombre + ' - ' + self.partido.equipo_visitante.nombre
