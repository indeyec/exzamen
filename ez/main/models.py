from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.crypto import get_random_string



def get_name_file(instance, filename):
    return '/'.join([get_random_string(length=5) + ' ' + filename])

class Product(models.Model):
    name = models.CharField(max_length=60, verbose_name='Название', blank=False)
    desc = models.CharField(max_length=250, verbose_name='Описание')
    photo = models.ImageField(upload_to=get_name_file, verbose_name='Фото', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'bmp'])])