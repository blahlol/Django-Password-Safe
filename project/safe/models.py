from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from passwordsafe.settings import PASS_KEY

# Create your models here.
class PassStore(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    website=models.CharField(max_length=100)
    username=models.CharField(max_length=150,default=None)
    password=models.CharField(max_length=200)

    def __str__(self):
        return str(self.username) +' '+ self.website
    
    def conv(self):
        key=Fernet(PASS_KEY)
        conv_pass=key.decrypt(bytes(self.password,'utf-8'))        
        return conv_pass.decode('utf-8')



        

        


