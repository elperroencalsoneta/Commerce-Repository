from django.db import models


class Supermarket(models.Model):
    name = models.CharField(max_length=255)
    photo =  models.URLField()
    address = models.CharField(max_length=255)
    open_state = models.TextField()
    operating_hours = models.TextField(max_length=200)
    website = models.URLField(max_length=255)
    distance = models.DecimalField(max_digits=6, decimal_places=2, default=0)


    def get_thumbnail(self):
            return  self.photo
    
    def __str__(self):
        return self.name

        #     MarketInfo[len(MarketInfo)] = {
        # "name": local_results[n]["title"],
        # "photo": local_results[n]['photos_link'],
        # "address": local_results[n]["address"],
        # "open_state": local_results[n]["open_state"],
        # "operating hours": local_results[n]["operating_hours"],
        # "website": website,
        # "distance from user": rounded_distance
     
