from django.db import models
from django.contrib.auth.models import User
import random
class Person(User):
    t=random.random()
    t=int(t*10000)
    otp=models.CharField(max_length=6,default=t)
    def __str__(self) -> str:
        return self.otp
    
