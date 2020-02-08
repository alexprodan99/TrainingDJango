from django.test import TestCase,SimpleTestCase




# Create your tests here.
#Django->automating testing
#SimpleTestCase -> we dont have database yet
#run:python manage.py test
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code,200)

