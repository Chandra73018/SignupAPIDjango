from django.db import models

# Create your models here.
class Register(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length = 100)
    email = models.EmailField(null=True,blank=True)
    mobile = models.CharField(null=True,blank=True,max_length=20)
    password = models.CharField(max_length = 200)
    confirm_password = models.CharField(max_length = 200)
