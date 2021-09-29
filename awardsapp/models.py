from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length =50)
    link = models.CharField(max_length =50)
    description = models.CharField(max_length =150)
    image = models.ImageField(upload_to = 'images/')
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

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects