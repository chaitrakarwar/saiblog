
from django.db import models
from django.conf import settings
# Create your models here.

class contact(models.Model):
    contact_id=models.AutoField(primary_key=True)
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Address=models.TextField()
    City=models.CharField(max_length=20)
    pin=models.IntegerField()
    mobile=models.DecimalField(max_digits=10,decimal_places=0)

    def show(self):
        self.save()
        
    def __str__(self):
        return self.First_Name


