from django.db import models

# Creador de modelos.
class Insumos(models.Model):
    cod         = models.IntegerField(primary_key=True)
    nombreinsumo= models.CharField(max_length=80)
    precio= models.IntegerField()
    descripcion= models.TextField()
    stock= models.IntegerField(default= 0)

    def _str__(self):
        return self.nombreinsumo

class Empleados(models.Model):
    cod         = models.IntegerField(primary_key=True)
    name        = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=20)
    imagen      = models.ImageField(upload_to='Empleados', null=True)

    def __str__(self):
        return self.name

class Slider(models.Model):
    cod = models.IntegerField(primary_key=True)
    imagen = models.ImageField(upload_to='Slider')

class Mision(models.Model):
    name        = models.CharField(max_length=20, primary_key=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.name

class Vision(models.Model):
    name        = models.CharField(max_length=20, primary_key=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.name

class Instalaciones(models.Model):
    cod       = models.IntegerField(primary_key=True)
    name      = models.CharField(max_length=30)
    direccion = models.TextField()
    imagen    = models.ImageField(upload_to='Instalaciones', null=True)

    def __str__(self):
        return self.name

class TipoContacto(models.Model):
    cod       = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Contacto(models.Model):
    cod       = models.IntegerField(primary_key=True)
    name      = models.CharField(max_length=50)
    lastname  = models.CharField(max_length=50)
    asunto    = models.CharField(max_length=50)
    tipoContacto = models.ForeignKey(TipoContacto,on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=200)

    def __str__(self):
        return self.name

