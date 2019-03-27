from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    zip = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name + ' - ' + self.city

class Interest(models.Model):
    interest = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.IntegerField()

    def __str__(self):
        return self.interest

class Language(models.Model):
    language = models.CharField(unique=True, max_length=100, blank=True, null=True)

    def __str__(self):
        return self.language

class Neighborhood(models.Model):
    neighborhood = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    map_image = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.neighborhood
