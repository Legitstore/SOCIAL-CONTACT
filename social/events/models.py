from django.db import models


# Create your models here.
class AddUser(models.Model):
    RELATIONSHIP = (
        ('Family', 'Family'),
        ('Friend', 'Friend'),   
        ('Brother', 'Brother'),   
        ('Sister', 'Sister'),   
        ('Mother', 'Mother'),   
        ('Father', 'Father'),   
        ('Cousin', 'Cousin'),
        ('In-Law', 'In-Law'),
        ('Others', 'Others'),
    )
    firstname = models.CharField(max_length=100, null=True,  blank=True)
    lastname = models.CharField(max_length=100, null=True,  blank=True)
    email = models.EmailField( null=True)
    phone = models.CharField(max_length=100, null=True,  blank=True)
    address = models.CharField(max_length=100, null=True,  blank=True)
    relationship = models.CharField(max_length=100, null=True,  blank=True, choices=RELATIONSHIP)