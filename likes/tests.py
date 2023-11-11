from django.contrib.auth.models import User
from posts.models import Post
from .models import Like
from rest_framework import status
from rest_framework.test import APITestCase


class LikeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user", password="pass")
        self.post = Post.objects.create(owner=self.user, content="Post content")

    def test_create_like(self):
        self.client.login(username="user", password="pass")
        response = self.client.post(
            f"/likes/", {"owner": self.user.id, "post": self.post.id}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Like.objects.count(), 1)
        self.assertTrue(Like.objects.filter(post=self.post, owner=self.user).exists())

    def test_retrieve_like(self):
        like = Like.objects.create(owner=self.user, post=self.post)
        response = self.client.get(f"/likes/{like.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], like.id)

    def test_delete_like(self):
        like = Like.objects.create(owner=self.user, post=self.post)
        self.client.login(username="user", password="pass")
        response = self.client.delete(f"/likes/{like.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Like.objects.count(), 0)

    def test_like_count_on_post(self):
        Like.objects.create(owner=self.user, post=self.post)
        response = self.client.get(f"/posts/{self.post.id}/")
        self.assertEqual(response.data["likes_count"], 1)
