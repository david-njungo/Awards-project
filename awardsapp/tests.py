from django.test import TestCase
from .models import Projects
# Create your tests here.
class ProjectsTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.delani = Projects(title = 'JDelani-Studio', description ='advertising a tech company',link = '')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.delani,Projects))
    
     # Testing Save Method
    def test_save_method(self):
        self.delani.save_project()
        projects = Projects.objects.all()
        self.assertTrue(len(projects) > 0)