from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Users(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre',max_length = 100)
    apellido = models.CharField('Apellido',max_length = 200)
    user_document=models.IntegerField('documento') 
    def __str__(self):
        return '{0}  {1}'.format(self.nombre,self.apellido)


# Create your models here.
