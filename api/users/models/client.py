from django.db import models

#Ultis 
from api.utils.models import BaseModel

class Client(BaseModel):
    """
        Modelo para el perfil del usuario
    """

    #Eliminar en cascada cuando se elimina un usuario
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'Imagen de perfil',
        upload_to = 'users/pictures',
        blank=True,
        null = True
    )
    biography = models.TextField(max_length=500, blank=True)

    #Estadisticas
    rides_taken = models.PositiveBigIntegerField(default=0)
    rides_offered = models.PositiveBigIntegerField(default=0)
    reputation = models.FloatField(
        default=5.0,
        help_text="Reputacion del usuario puntuacion asiganada por un usuario externo"
    )

    def __str__(self):
        return str(self.user)
    


