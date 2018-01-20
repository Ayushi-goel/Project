from django.test import TestCase
from django.core.urlresolvers import reverse
from django.urls import resolve
from .views import home,plant_info
from .models import Plants

class HomeTests(TestCase):
   def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

   def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

class PlantInfoTests(TestCase):
    def setUp(self):
        Plants.objects.create(Name='Abronia bigelovii', Species_id='Species_id 1')

    def test_plant_info_view_success_status_code(self):
        url = reverse('plant_info', kwargs={'pk': 21})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_plant_info_view_not_found_status_code(self):
        url = reverse('plant_info', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_plant_info_url_resolves_plant_info_view(self):
        view = resolve('/plants/1/')
        self.assertEquals(view.func, plant_info)

# Create your tests here.
