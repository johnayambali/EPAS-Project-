from django.test import TestCase

from projectListing.models import *

class TestModels(TestCase):

    def setUp(self):
        self.testUser = User.objects.create_user(
            username='user',
            password='test',
            type='student',
        )

    def test_user_has_correct_type(self):
        self.assertEquals(self.testUser.type, 'student')


    #get_absolute_Url is hard coded in models thus not tested

