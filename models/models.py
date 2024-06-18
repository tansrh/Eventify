from django.db import models
class Event(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    date=models.TextField()
    time=models.TextField()
    location=models.CharField(max_length=200)
    capacity=models.IntegerField()
    
class Attendee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100,primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  
    





# Create your models here.
