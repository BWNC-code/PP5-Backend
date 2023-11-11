from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.post = Post.objects.create(
            owner=self.user, title="Test Post", content="Just a test post"
        )

    def test_post_creation(self):
        self.client.login(username="testuser", password="testpass123")
        data = {"title": "New Post", "content": "Content of the new post"}
        response = self.client.post("/posts/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.latest("id").title, "New Post")

    def test_post_list(self):
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data.get("results", [])
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Test Post")

    def test_post_detail(self):
        response = self.client.get("/posts/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Post")
        self.assertEqual(response.data["content"], "Just a test post")

    def test_post_update(self):
        self.client.login(username="testuser", password="testpass123")
        data = {"title": "Updated Post", "content": "Updated content"}
        response = self.client.put("/posts/1/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "Updated Post")

    def test_post_delete(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.delete("/posts/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)
