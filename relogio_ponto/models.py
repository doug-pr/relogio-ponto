from django.db import models

# Create your views here.
class Horario(models.Model):
    entrada_1 = models.DateTimeField()
    saida_1 = models.DateTimeField(null=True)
    entrada_2 = models.DateTimeField(null=True)
    saida_2 = models.DateTimeField(null=True)
    entrada_3 = models.DateTimeField(null=True)
    saida_3 = models.DateTimeField(null=True)