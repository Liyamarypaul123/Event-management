from django.db import models

# Create your models here.
class Event(models.Model):
    event_title=models.CharField(max_length=120)
    location=models.CharField(max_length=60)
    date=models.CharField(max_length=120)
    description=models.TextField()

    def __str__(self):
        return self.event_title
    
    
class Applicant(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    event=models.ForeignKey('Event',on_delete=models.CASCADE)

    def __str__(self):
        return self.name