from django.db import models

from api.utils.models import BaseModel

class Circles(BaseModel):
    """
        Modelo de ciculo

        Un circulo es una area en la cual puedes ser parte y de la cual puede unirte para
        formar parte de ducho circulo tiene que ser invitado por un miembro del circulo
    """
    name = models.CharField('Nombre del circulo', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)

    about = models.CharField('Descripcion del circulo', max_length=250)
    picture = models.ImageField(upload_to='circles/pictures', blank=True, null=True)

    rides_offered = models.PositiveBigIntegerField(default=0)
    rides_taken = models.PositiveBigIntegerField(default=0)

    verified = models.BooleanField(
        'Circulo verificado',
        default=False,
        help_text="Circulo verificado por las autoridades"
    )

    public = models.BooleanField(default= True, help_text="Circulos publicos para que puedan ser visibles para todos los usuarios")

    is_limit = models.BooleanField(
        'Limitado',
        default=False,
        help_text='Limitar un grupo unicamente para una cantidad establecidad de usuarios'
    )
    member_limit = models.PositiveBigIntegerField(
        default=0,
        help_text="En el caso que el usuario sea limitado se establece la cantidad de usuarios que pueden ingresar"
    )

    def __str__(self):
        return self.name


    class Meta(BaseModel.Meta):
        ordering = ['-rides_taken', '-rides_offered']




