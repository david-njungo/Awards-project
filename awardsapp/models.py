from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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


class Profile(models.Model):
    prof_photo = models.ImageField(upload_to = 'profile/')
    bio = models.TextField(max_length=500, blank=True)
    contact = models.CharField(max_length=60,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()