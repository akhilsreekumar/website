from django.db import models

# Create your models here.

class Temper(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(default=0)

    def __str__(self):
        return str(self.value)

    class Meta:
        ordering = ('created',)

class Pressure(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(default=0)

    def __str__(self):
        return str(self.value)

    class Meta:
        ordering = ('created',)

class HeartBeat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(default=0)

    def __str__(self):
        return str(self.value)

    class Meta:
        ordering = ('created',)

class Glucose(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(default=0)

    def __str__(self):
        return str(self.value)

    class Meta:
        ordering = ('created',)