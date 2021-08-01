from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse, resolve
# from .apps import HomepageConfig
# from .models import Status
# from .forms import StatusInput
from . import views


# class HomePageTests(TestCase):
#     def test_apps(self):
#         self.assertEqual(HomepageConfig.name, 'homepage')
    
#     def test_homepage_status_code(self):
#         response = self.client.get('')
#         self.assertEquals(response.status_code, 200)

#     def test_view_url_by_name(self):
#         response = self.client.get(reverse('homepage:index'))
#         self.assertEquals(response.status_code, 200)

#     def test_view_uses_correct_template(self):
#         response = self.client.get(reverse('homepage:index'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'homepage.html')

#     def test_homepage_contains_correct_html(self):
#         response = self.client.get('')
#         self.assertContains(response, "<title>Afriza's StorySix</title>")

#     def test_homepage_does_not_contain_incorrect_html(self):
#         response = self.client.get('')
#         self.assertNotContains(response, '{% extends "base.html" %}')
    
#     def test_homepage_uses_correct_view(self):
#         func = resolve('/')
#         self.assertEqual(views.index, func.func)
    
#     def test_model_can_create_new_status(self):
#         status = Status.objects.create(status='Hi!')

#         count = Status.objects.all().count()
#         self.assertEqual(count, 1)
    
#     def test_form_validation_for_blank_items(self):
#         form = StatusInput(data={'status': ''})
#         self.assertFalse(form.is_valid())
#         self.assertEqual(
#             form.errors['status'],
#             ["This field is required."]
#         )
    
#     def test_form_validation_for_filled_items(self) :
#         response = self.client.post('', data={'status' : 'Hi!'})
#         response_content = response.content.decode()
#         self.assertIn(response_content, 'Hi!')

#     def test_form_name(self) :
#         response = self.client.post('', data={'status' : 'Hi!'})
#         status = Status.objects.get(pk=1)
#         self.assertEqual(str(status), status.status)
    
#     def test_post_success_and_render_the_result(self):
#         test = "I'm a Test."
#         response_post = self.client.post('', {'status': test})
#         self.assertEqual(response_post.status_code, 302)

#         response = self.client.get('')
#         self.assertEqual(response.context['all_status'].get(status=test).status, test)