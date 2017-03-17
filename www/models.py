from django.db import models

# Create your models here
class Category(models.Model):
    name = models.CharField(max_length = 20)
    first_year = models.PositiveSmallIntegerField()
    secon_year = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
        
class Runner(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    birtday = models.DateField(auto_now=False, auto_now_add=False)
    category = models.ForeignKey(Category)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name
