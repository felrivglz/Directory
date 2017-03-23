from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here
class Category(models.Model):
    name = models.CharField(max_length = 20)
    first_year = models.PositiveSmallIntegerField()
    secon_year = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Competition(models.Model):
     name = models.CharField(max_length = 40)
     place = models.CharField(max_length = 30)
     weather = models.CharField(max_length =200)
     date = models.DateField(auto_now=False, auto_now_add=False)

     def __str__(self):
        return self.name


class Runner(models.Model):
    DISTANCE = (
                    ('100', '100 Metros Planos'),
                    ('200', '200 Metros Planos'),
                    ('400', '400 Metros Planos'),
                    ('800', '800 Metros Planos'),
                    ('1500', '1500 Metros Planos'),
                    ('3000', '3000 Metros Planos'),
                    ('5000', '5000 Metros Planos'),
                    ('10000', '10000 Metros Planos'),
                    ('110v', '110 Metros Con Vallas'),
                    ('400v', '400 Metros Con Vallas'),
                )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birtday = models.DateField(auto_now=False, auto_now_add=False)
    category = models.ForeignKey(Category)
    coach = models.ForeignKey(User)
    distance = models.CharField(max_length=10, choices=DISTANCE)
    image = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            name = self.first_name + ' ' + self.last_name
            self.slug = slugify(name)
            super(Runner, self).save(self, *args, **kwargs)

    def __str__(self):
        return self.first_name


class Metas(models.Model):
    meta = models.CharField(max_length=200)
    runner = models.ForeignKey(Runner)

    def __str__(self):
       return self.meta



class Time(models.Model):
    DISTANCE = (
                   ('100', '100 Metros Planos'),
                    ('200', '200 Metros Planos'),
                    ('400', '400 Metros Planos'),
                    ('800', '800 Metros Planos'),
                    ('1500', '1500 Metros Planos'),
                    ('3000', '3000 Metros Planos'),
                    ('5000', '5000 Metros Planos'),
                    ('10000', '10000 Metros Planos'),
                    ('110v', '110 Metros Con Vallas'),
                    ('400v', '400 Metros Con Vallas'),
               )
    distance = models.CharField(max_length=10, choices=DISTANCE)
    time = models.CharField(max_length=10)
    compentition = models.ForeignKey(Competition)
    runner = models.ForeignKey(Runner)


    def __str__(self):
        return self.time
