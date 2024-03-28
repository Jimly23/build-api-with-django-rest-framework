from django.db import models

# Create your models here.
class Kontak(models.Model):
    username = models.CharField(max_length=100)
    telp = models.CharField(max_length=15)
    alamat = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)

    def __str__(self) -> str:
        return self.username