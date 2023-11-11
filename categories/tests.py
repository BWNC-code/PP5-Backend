from .models import Category
from rest_framework import status
from rest_framework.test import APITestCase


class CategoryTests(APITestCase):
    def setUp(self):
        Category.objects.create(name="Adventure", description="Adventure related posts")

    def test_create_category(self):
        self.assertEqual(Category.objects.count(), 1)
        category = Category.objects.first()
        self.assertEqual(category.name, "Adventure")

    def test_retrieve_category(self):
        category = Category.objects.first()
        response = self.client.get(f"/categories/{category.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Adventure")
