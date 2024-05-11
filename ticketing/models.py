from django.db import models

# Create your models here.
DESTINATIONS = (
    ('US', 'United States'),
    ('CA', 'Canada'),
    ('UK', 'United Kingdom'),
)

class State(models.Model):
    name = models.CharField(max_length = 250)

    def __str__(self):
        return self.name

class Destination(models.Model):
    name = models.CharField(max_length = 250)
    state = models.ForeignKey(State, on_delete = models.CASCADE)
    

    def __str__(self):
        return self.name


class Passenger(models.Model):
    destination = models.ForeignKey(Destination, on_delete = models.CASCADE)
    fare = models.IntegerField(default = 0)
    fingerprint = models.CharField(max_length = 200)
    paid = models.BooleanField(default = False)
    amt_paid = models.IntegerField(default = 0)

    def __str__(self):
        return self.destination.name
    

