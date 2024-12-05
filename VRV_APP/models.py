from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser 

from django.db import models
from django.contrib.auth.models import User
Token_choices=(
    ('DEACTIVE','Deactive'),
    ('ACTIVE','Active')
)
class userdetails(models.Model):
    client=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=10, unique=True) 
    dob = models.DateField()
    user_token = models.CharField(max_length=10000,unique=True,null=True)
    user_type = models.CharField(max_length=100,null=True)
    token_creation_time=models.DateTimeField(null=True,blank=True)
    status=models.CharField(max_length=100,choices=Token_choices,null=True,blank=True)

    def __str__(self):
        return self.phone
