from django.test import TestCase, Client
from django.urls import resolve
from .views import home, about, services

# Create your tests here.
class UnitTest(TestCase):

    # home
    def test_main_url_exists(self):
        response = Client().get("")
        self.assertEqual(response.status_code, 200)
    
    def test_return_main_html(self):
        response = Client().get("")
        self.assertTemplateUsed(response, "InfoPage/home.html")

    def test_main_view_func(self):
        found = resolve("/")
        self.assertEqual(found.func, home)
    
    # About 
    def test_about_url_exists(self):
        response = Client().get("/about/")
        self.assertEqual(response.status_code, 200)
    
    def test_return_about_html(self):
        response = Client().get("/about/")
        self.assertTemplateUsed(response, "InfoPage/about.html")

    def test_about_view_func(self):
        found = resolve("/about/")
        self.assertEqual(found.func, about)

    # Services
    def test_services_url_exists(self):
        response = Client().get("/services/")
        self.assertEqual(response.status_code, 200)
    
    def test_services_main_html(self):
        response = Client().get("/services/")
        self.assertTemplateUsed(response, "InfoPage/services.html")

    def test_services_view_func(self):
        found = resolve("/services/")
        self.assertEqual(found.func, services)

   