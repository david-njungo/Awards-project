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