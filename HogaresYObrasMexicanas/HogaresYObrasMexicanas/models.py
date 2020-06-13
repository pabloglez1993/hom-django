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

class Partida(models.Model):
    nombre = models.CharField(max_length=50)
    conceptos = models.ForeignKey("Concepto", on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return "{}".format(self.nombre)

class Proyecto(models.Model):
    titulo = models.CharField(max_length=50)
    propietario = models.CharField(max_length=50)
    direccion = models.OneToOneField("Direccion", on_delete=models.CASCADE)
    presupuesto = models.FloatField()
    partidas = models.ForeignKey("Partida", on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return "{}".format(self.titulo)

class Concepto(models.Model):
    nombre = models.CharField(max_length=50)
    unidades = models.ForeignKey("Unidad", on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return "{}".format(self.nombre)

    @property
    def get_total_unidades(self):
        total_unidades = self.unidades.objects.all()
        print(total_unidades)
        return total_unidades

class Unidad(models.Model):
    nombre = models.CharField(max_length=50)
    precio_unitario = models.FloatField()
    cantidad = models.FloatField()
    class Meta:
        verbose_name_plural = 'Unidades'  
    
    @property
    def total(self):
        return self.precio_unitario * self.cantidad

    