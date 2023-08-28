from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r"^09(1[0-9]|3[1-9])-?[0-9]{3}-?[0-9]{4}$")

def upload_path(instance,title):
    name = instance.username
    return f'images/{name}.jpg'

class Contact(AbstractUser):
    image = models.ImageField(upload_to=upload_path)
    phone = models.CharField(validators=[phone_regex], max_length=20)
    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)

class Feedback(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title

