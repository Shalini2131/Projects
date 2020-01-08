from django.db import models

# Create your models here.
class SignUp(models.Model):
    first_name=models.CharField(max_length=20)
    # last_name=models.CharField(max_length=20)
    email_add=models.EmailField(max_length=200)
class login(models.Model):
    email:models.EmailField(max_length=200)
 