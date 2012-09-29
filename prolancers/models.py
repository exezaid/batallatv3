# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


CAT_FREELANCER = 'freelancer'
CAT_EMPRESA = 'empresa'


class Prolancer(models.Model):
    user = models.ForeignKey('auth.User')
    categoria = models.CharField(max_length=200, choices=(
        (CAT_FREELANCER, 'Freelancer'), (CAT_EMPRESA, 'Empresa')))
    descripcion = models.TextField(blank=True)
    direccion = models.CharField(u'Dirección', max_length=200)
    mail_empresa = models.EmailField()
    imagen = models.ImageField(blank=True, upload_to=settings.MEDIA_ROOT)

    contador = models.IntegerField(null=True)
    publicado = models.BooleanField()
    oculto = models.BooleanField()
    creado = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.user.get_full_name()

    @property
    def nombre_empresa(self):
        if self.categoria == CAT_EMPRESA:
            return self.user.first_name
