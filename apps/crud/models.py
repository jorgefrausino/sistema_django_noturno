from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    # adicione aqui os outros campos do seu formulário

    def __str__(self):
        return self.nome