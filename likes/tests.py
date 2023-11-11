from django.contrib.auth.models import User
from posts.models import Post
from .models import Like
from rest_framework.test import APITestCase

class LikeTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username="user", password="pass")
        post = Post.objects.create(owner=user, content="Post content")
        Like.objects.create(owner=user, post=post)

    def test_like_post(self):
        self.assertEqual(Like.objects.count(), 1)
        like = Like.objects.first()
        self.assertIsNotNone(like)

    def test_retrieve_like(self):
        like = Like.objects.first()
        response = self.client.get(f"/likes/{like.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
