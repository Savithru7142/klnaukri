from django.db import models

# Create your models here.
class Useraccount(models.Model):
    ROLE_CHOICES = [
        ('employer', 'Employer'),
        ('jobseeker', 'Jobseeker'),
    ]
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(primary_key=True)
    phonenumber=models.CharField(max_length=20)
    role=models.CharField(max_length=10, choices=ROLE_CHOICES)
    password=models.CharField(max_length=120)
    def __str__(self):
        return self.firstname

