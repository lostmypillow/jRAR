from django.db import models



class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)
    department = models.BigAutoField
    birthdate = models.DateField(null=True, blank=True)
    cv = models.FileField(null=True, blank=True)

class Card(models.Model):
    values = models.CharField(max_length=200)
    auth = models.BooleanField(default=True)
