"""Django models utilities."""

# Django
from django.db import models


class BaseModel(models.Model):
    """modelo base de proyecto.

    BaseModel actúa como una clase base abstracta de la cual cada
    otro modelo en el proyecto heredará. Esta clase proporciona
    cada tabla con los siguientes atributos:
        + created (DateTime): almacena la fecha y hora en que se creó el objeto.
        + modified (DateTime): almacena la última fecha y hora en que se modificó el objeto.
    """

    created = models.DateTimeField(
        'creado en',
        auto_now_add=True,
        help_text='Fecha en la que fue creado el registro.'
    )
    modified = models.DateTimeField(
        'mmodificado en',
        auto_now=True,
        help_text='Fecha en la que fue modificado el registro.'
    )

    class Meta:
        """Meta option."""

        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']
