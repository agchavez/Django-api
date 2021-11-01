"""
    User model.
"""

#Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

#Utils
from api.utils.models import BaseModel

class User(BaseModel, AbstractUser):
    """
        Extiende de la calses Base model, la clase AbsractUser que nos ofrece python
    """
    email = models.EmailField(
        'correo electronico',
        unique=True,
        error_messages={
            'unique':'El correo electronico ya existe. utilice el formato +50499935566'
        }
    )
    USERNAME_FIELD = 'email'
    phone_regex = RegexValidator(
        regex=r'\+?504?\d{9,15}$',
        message="El numero de telefono no es valido"
    )
    phone_number = models.CharField(validators=[phone_regex] , max_length=16, blank=True)


    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'cliente',
        default=True,
        help_text=(
            'Tipo de usuario que se registra en la plataforma'
        )
    )

    id_verified = models.BooleanField(
        'verificado',
        default=True, 
        help_text='Si el usuario ha verifacado su correo electronico'
    )

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username