from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#https://stackoverflow.com/questions/31130706/dropdown-in-django-model /// dropdown django
COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)
class info_tp(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    nome_prof = models.CharField(max_length=100)
    imail_prof = models.CharField(max_length=100)
    nome_modul = models.CharField(max_length=100)
    type_shm = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')
    title_tp = models.CharField(max_length=100)
    description_tp = models.CharField(max_length=500)
    fiche_tp = models.FileField(upload_to='uploads/')
    img = models.ImageField(upload_to='info_tp_img/')

    def __str__(self):

        return self.title_tp

