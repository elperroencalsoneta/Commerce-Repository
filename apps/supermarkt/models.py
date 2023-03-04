from django.db import models


class Supermarkt(models.Model):
    name = models.CharField(max_length=255)
    photo =  models.URLField()
    address = models.CharField(max_length=255)
    open_state = models.CharField(max_length=255, default='')
    operating_hours = models.CharField(max_length=200)
    website = models.URLField(max_length=255)
    distance = models.DecimalField(max_digits=6, decimal_places=2, default=0)


    def get_thumbnail(self):
            return  self.image
    
    def __str__(self):
        return self.name