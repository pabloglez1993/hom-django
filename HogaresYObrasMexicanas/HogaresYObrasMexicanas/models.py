from django.db import models

class Direccion(models.Model):
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    colonia = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    codigo_postal = models.IntegerField()

    def __str__(self):
        return "{} {} {} {}".format(self.calle,self.numero,self.colonia,self.codigo_postal)
    class Meta:
        verbose_name_plural = 'Direcciones'    


class Proyecto(models.Model):
    titulo = models.CharField(max_length=50)
    propietario = models.CharField(max_length=50)
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE)
    presupuesto = models.FloatField()
    def __str__(self):
        return "{}".format(self.titulo)

class Partida(models.Model):
    nombre = models.CharField(max_length=50)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    def __str__(self):
        return "{}".format(self.nombre)

class Concepto(models.Model):
    nombre = models.CharField(max_length=50)
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    def __str__(self):
        return "{}".format(self.nombre)

class Unidad(models.Model):
    nombre = models.CharField(max_length=50)
    concepto = models.ForeignKey(Concepto, on_delete=models.CASCADE)
    precio_unitario = models.FloatField()
    cantidad = models.FloatField()
    class Meta:
        verbose_name_plural = 'Unidades'    