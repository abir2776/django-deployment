from tkinter import CASCADE
from django.db import models

class musician(models.Model):
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    instrument= models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name

class album(models.Model):
    artist= models.ForeignKey(musician,on_delete=models.CASCADE)
    name= models.CharField(max_length=50)
    release_date= models.DateField()
    rating = (
        (1,"Bad"),
        (2,"Not Bad"),
        (3,"Average"),
        (4,"Good"),
        (5,"Excellent"),
    )
    num_star= models.IntegerField(choices=rating)
    def __str__(self):
        return self.name + ", Rating:"+str(self.num_star)
# Create your models here.
