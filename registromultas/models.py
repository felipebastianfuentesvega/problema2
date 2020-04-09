# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Inspectores(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    rut = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inspectores'


class MultasEstacionamiento(models.Model):
    patente = models.CharField(max_length=6, blank=True, null=True)
    fechayhora = models.DateTimeField(blank=True, null=True)
    lugar = models.CharField(max_length=200, blank=True, null=True)
    pagada = models.IntegerField(blank=True, null=True)
    inspectorid = models.ForeignKey(Inspectores, models.DO_NOTHING, db_column='inspectorid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'multas_estacionamiento'
