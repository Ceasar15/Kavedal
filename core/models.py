from django.db import models

# Create your models here.

class ContactModel(models.Model):
    name = models.CharField(max_length=250, null=True)
    email = models.EmailField(null=True)
    subject = models.TextField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']	

    def __str__(self):
        return self.name