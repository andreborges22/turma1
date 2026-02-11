from django.db import models
# Create your models here.
class Aluno(models.Model):    
    nome = models.CharField(max_length=100)

    def __init__(self):
        return super().__str__()