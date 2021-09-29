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

    def tearDown(self):
        Projects.objects.all().delete()

    def test_get_projects(self):
        get_projects = Projects.get_project()
        self.assertTrue(len(get_projects)==0)