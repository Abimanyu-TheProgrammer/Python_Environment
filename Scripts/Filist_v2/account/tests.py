from django.test import TestCase, Client
from django.urls import resolve
from .views import registerUser

# Create your tests here.
def test_register_url_exists(self):
    response = Client().get("/register/")
    self.assertEqual(response.status_code, 200)
    
def test_return_register_html(self):
    response = Client().get("/register/")
    self.assertTemplateUsed(response, "account/register.html")

def test_register_view_func(self):
    found = resolve("/register/")
    self.assertEqual(found.func, registerUser)