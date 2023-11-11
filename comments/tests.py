from django.contrib.auth.models import User
from posts.models import Post
from .models import Comment
from rest_framework import status
from rest_framework.test import APITestCase


class CommentTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username="user", password="pass")
        post = Post.objects.create(owner=user, content="Post content")
        Comment.objects.create(owner=user, post=post, content="Comment content")

    def test_create_comment(self):
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.first()
        self.assertEqual(comment.content, "Comment content")

    def test_retrieve_comment(self):
        comment = Comment.objects.first()
        response = self.client.get(f"/comments/{comment.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["content"], "Comment content")
