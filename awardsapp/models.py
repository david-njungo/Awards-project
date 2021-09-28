from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length =30)
    link = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    # image
    def __str__(self):
        self.title
