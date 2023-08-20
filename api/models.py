from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    number = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return "%s-%s-%s-%s" % (
            self.id , self.name , self.email, self.number
        )
