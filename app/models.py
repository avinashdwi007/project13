from django.db import models

# Create your models here.

class Employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField(max_length=100)
    eactive = models.CharField(max_length=10, default='Active') 
    epassword = models.CharField(max_length=100)

    def __str__(self):
        return self.ename