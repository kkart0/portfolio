from django.db import models

# Create your models here.
class Project(models.Model):
    Project_name=models.CharField       (max_length=100,default="")
    Project_language=models.CharField   (max_length=100,default="")
    Project_discription=models.CharField(max_length=1000,default="")
    Project_image=models.ImageField     (default="")
    
    def __str__(self):
        return self.Project_name

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.CharField(max_length=1000)
    def __str__(self):
        return self.name
    