from django.db import models

class Ports(models.Model):
    name = models.CharField(max_length = 26)
    number = models.IntegerField(default = 1)
    type = models.CharField(max_length = 3, default='TCP')

    def __str__(self):
        return self.name