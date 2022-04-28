from django.test import TestCase
from projectListing.forms import PostForm
from django.utils import timezone
from projectListing.models import *


#checks if form is valid and if its not

class TestForms(TestCase):


    def test_post_form_is_valid(self):
        self.testProf = User.objects.create_user(
            username='user',
            password='test',
            type='professor',
        )

        form = PostForm(data={
            'title': 'testProj',
            'description': 'testDesc',
            'date_posted': '2022-04-23',
            'professor': self.testProf.id,
            'desiredNumStudents': 2,
            'maxNumStudents': 3,
            'minTermLength': 4,
            'maxTermLength': 8,
            'relatedProgram': 'Comp Sci',
            'course': 'CSI4900',
            'active': True
        })
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_post_form_no_data(self):
        form = PostForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 8)