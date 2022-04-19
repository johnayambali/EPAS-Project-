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
        self.postcreate_url = reverse('post-create')
        self.postdetail_url = reverse('post-detail', args=[2016])
        self.postupdate_url = reverse('post-update', args=[2023])
        self.postdelete_url = reverse('post-delete', args=[2026])
        self.postapprove_url = reverse('post-approval', args=[2320])
        self.appcreate_url = reverse('application-create', args=[2320])
        self.appdetail_url = reverse('application-detail', args=[2420])
        self.appupdate_url = reverse('application-update', args=[2920])
        self.appdelete_url = reverse('application-delete', args=[2520])
        self.appstatus_url = reverse('application-status', args=[2520])
        self.appoffer_url = reverse('application-offer', args=[2520])
        self.profproj_url = reverse('projectListing-prof_myprojects')
        self.profapp_url = reverse('projectListing-prof_projectapplication')
        self.profactive_url = reverse('projectListing-prof_myactiveprojects')
        self.profprofile_url = reverse('projectListing-prof_profile')


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
        response = self.client.get(self.myprojects_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projectListing/myprojects.html')

    def test_applications_GET(self):
        response = self.client.get(self.app_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projectListing/applications.html')

    def test_profprofile_GET(self):
        response = self.client.get(self.profprofile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projectListing/prof_profile.html')

    def test_profprojects_GET(self):
        response = self.client.get(self.profproj_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projectListing/prof_myprojects.html')


    '''def test_postdetailview_GET(self):
        response = self.client.get(self.postdetail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projectListing/post_detail.html')'''

