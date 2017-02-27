from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=20, blank=False)
    apellido = models.CharField(max_length=25, blank=False)
    legajo = models.IntegerField(blank=False, unique=True)
    grado = models.CharField(max_length=15,
        choices=(('Bombero', 'Bombero'),
        ('Cabo', 'Cabo'),
        ('Cabo 1°', 'Cabo 1°'))
        )

    def __str__(self):
        return '{} {}'.format(self.apellido, self.nombre)


class Ropa(models.Model):
    funcion_de_la_ropa = models.CharField(
            max_length=14,
            choices=(
                ('Incendio', 'Incendio'),
                ('Rescate', 'Rescate'),
                ('Fajina', 'Fajina'),
                ('Mameluco', 'Mameluco')
                )
            )
    inventario = models.IntegerField(blank=False, unique=True)

    def __str__(self):
        return self.funcion_de_la_ropa

    class Meta:
        abstract = True


class RopaDeIncendio(Ropa):
    prenda = models.CharField(
        max_length=15,
        choices=(
            ('Casco', 'Casco'),
            ('Monja', 'Monja'),
            ('Guantes', 'Guantes'),
            ('Saco', 'Saco')
        )
    )
    comodatario = models.ForeignKey(Persona,
        on_delete=models.CASCADE,
        default='1',
    )

    def __str__(self):
        return self.prenda
