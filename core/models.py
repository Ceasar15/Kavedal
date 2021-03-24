from django.db import models

# Create your models here.

class ContactModel(models.Model):
    name = models.CharField(max_length=250, null=True)
    email = models.EmailField(null=True)
    subject = models.TextField()
    message = models.TextField()
