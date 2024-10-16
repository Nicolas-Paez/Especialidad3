from django.db import models

class Formulario(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Pregunta(models.Model):
    formulario = models.ForeignKey(Formulario, related_name='preguntas', on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    es_correcta = models.BooleanField(default=False)

class Resultado(models.Model):
    estudiante_id = models.CharField(max_length=255)
    respuestas = models.JSONField()  # Se guardarán las respuestas seleccionadas en formato JSON
    nota = models.FloatField()

    def __str__(self):
        return f'Estudiante {self.estudiante_id} - Nota: {self.nota}'
