from django.db import models

class login(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.BigIntegerField(blank=True, default=0)

    def __str__(self):
        return f"{self.name} {self.email} {self.password} {self.phone}"
