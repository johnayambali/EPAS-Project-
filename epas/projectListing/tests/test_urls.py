from django.test import SimpleTestCase
from django.urls import reverse, resolve

from projectListing.views import *
#home, homeDirector, profile, myprojects, applications, projectapplication, PostListView, projectapply, profprofile,
from users.views import profile

#This tests all the urls in **projectListing**
#Tests using reverse and resolve
#pk  = primary key


class TestUrls(SimpleTestCase):
    #done for all the urls

    #Tests for posts urls
    def test_home_url_resolves(self):
        url = reverse('projectListing-home')
        self.assertEquals(resolve(url).func, home)

    def test_profile_url_resolves(self):
        url = reverse('projectListing-profile')
        #print(resolve(url))
        self.assertEquals(resolve(url).func, profile)

    def test_homedirector_url_resolves(self):
        url = reverse('projectListing-homeDirector')
        self.assertEquals(resolve(url).func, homeDirector)

    def test_myprojects_url_resolves(self):
        url = reverse('projectListing-myprojects')
        self.assertEquals(resolve(url).func, myprojects)

    def test_applications_url_resolves(self):
        url = reverse('projectListing-applications')
        self.assertEquals(resolve(url).func, applications)



    #Tests for Posts urls
    def test_postcreate_url_resolves(self):
        url = reverse('post-create')
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_postdetail_url_resolves(self):
        url = reverse('post-detail', args=[2016])
        self.assertEquals(resolve(url).func.view_class, PostDetailView)

    def test_postupdate_url_resolves(self):
        url = reverse('post-update', args=[2023])
        self.assertEquals(resolve(url).func.view_class, PostUpdateView)

    def test_postdelete_url_resolves(self):
        url = reverse('post-delete', args=[2026])
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)

    #Tests for Application urls
    def test_appcreate_url_resolves(self):
        url = reverse('application-create', args=[2320])
        self.assertEquals(resolve(url).func.view_class, ApplicationCreateView)

    def test_appdetail_url_resolves(self):
        url = reverse('application-detail', args=[2420])
        self.assertEquals(resolve(url).func.view_class, ApplicationDetailView)

    def test_appupdate_url_resolves(self):
        url = reverse('application-update', args=[2920])
        self.assertEquals(resolve(url).func.view_class, ApplicationUpdateView)

    def test_appdelete_url_resolves(self):
        url = reverse('application-delete', args=[2520])
        self.assertEquals(resolve(url).func.view_class, ApplicationDeleteView)

    def test_updatestatus_url_resolves(self):
        url = reverse('application-status', args=[2520])
        self.assertEquals(resolve(url).func.view_class, UpdateStatusView)

    def test_updateoffer_url_resolves(self):
        url = reverse('application-offer', args=[2520])
        self.assertEquals(resolve(url).func.view_class, UpdateOfferView)

    def test_profprojapp_url_resolves(self):
        url = reverse('projectListing-prof_projectapplication')
        self.assertEquals(resolve(url).func, profprojectapplications)

    def test_profactiveproj_url_resolves(self):
        url = reverse('projectListing-prof_myactiveprojects')
        self.assertEquals(resolve(url).func, profmyactiveprojects)



