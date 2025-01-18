from django.db import models

# Create your models here.
class userdata(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.email
    
class image(models.Model):
    dr_image=models.ImageField(upload_to='images/')
    dr_name=models.CharField(max_length=50)
    dr_prof=models.CharField(max_length=100)
    summary=models.CharField(max_length=500)

    def __str__(self):
        return self.dr_name

# class slot(models.Models):
