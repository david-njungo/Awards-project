from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length =30)
    link = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    # Rates
    # user
    def __str__(self):
       return self.title
    class Meta:
        ordering = ['title'] 

    def save_project(self):
        self.save() 
    @classmethod  
    def get_project(cls):
        projects = cls.objects.all()
        return projects
