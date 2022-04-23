from django.test import TestCase, Client
from django.urls import reverse
from projectListing.models import *
import json

#Tests both GET & POST
#***Tests for the views of Posts, Applications, & Application updates in views.py ***

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('projectListing-home')
        self.hd_url = reverse('projectListing-homeDirector')
        self.profile_url = reverse('projectListing-profile')
        self.myprojects_url = reverse('projectListing-myprojects')
        self.app_url = reverse('projectListing-applications')

        self.profactive_url = reverse('projectListing-prof_myactiveprojects')
        self.profapp_url = reverse('projectListing-prof_projectapplication')

        self.testUser = User.objects.create_user(
            username='user',
            password='test',
            type='student',
        )


#Functional Views tested
    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projectListing/home.html')

    def test_homedirector_GET(self):
        response = self.client.get(self.hd_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projectListing/home_director.html')

    def test_profile_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projectListing/home.html')


    def test_myprojects_GET(self):
        login = self.client.login(username='user', password='test')
        response = self.client.get(self.myprojects_url)
        self.assertTrue(login)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projectListing/myprojects.html')


    def test_applications_GET(self):
        login = self.client.login(username='user', password='test')
        response = self.client.get(self.app_url)
        self.assertTrue(login)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projectListing/applications.html')

    def test_prof_proj_app_GET(self):
        login = self.client.login(username='user', password='test')
        response = self.client.get(self.profapp_url)
        self.assertTrue(login)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projectListing/prof_projectapplications.html')

    def test_prof_active_proj_GET(self):
        login = self.client.login(username='user', password='test')
        response = self.client.get(self.profactive_url)
        self.assertTrue(login)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projectListing/prof_myactiveprojects.html')





