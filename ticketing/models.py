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
    destination = models.ForeignKey(Destination, on_delete = models.CASCADE, null=True)
    fare = models.IntegerField(default = 0, blank=True)
    fingerprint = models.CharField(max_length = 200, blank=True)
    paid = models.BooleanField(default = False, blank=True)
    amt_paid = models.IntegerField(default = 0, blank=True)

    def __str__(self):
        if self.destination != None:
            return self.destination.name
        else:
            return self.fingerprint
    

