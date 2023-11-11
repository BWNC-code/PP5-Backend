from django.contrib.auth.models import User
from posts.models import Post
from .models import Comment
from rest_framework import status
from rest_framework.test import APITestCase

class CommentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user", password="pass")
        self.post = Post.objects.create(owner=self.user, content="Post content")
        self.comment = Comment.objects.create(owner=self.user, post=self.post, content="Comment content")

    def test_create_comment(self):
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(self.comment.content, "Comment content")

    def test_retrieve_comment(self):
        response = self.client.get(f"/comments/{self.comment.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["content"], "Comment content")

    # logs in as the user, updates the comment content, and verifies that the update was successful
    def test_edit_comment(self):
        self.client.login(username="user", password="pass")
        updated_content = "Updated Comment Content"
        response = self.client.put(f"/comments/{self.comment.id}/", {"content": updated_content})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, updated_content)

    # logs in as the user, deletes the comment, and verifies that the comment was
    # successfully removed from the database
    def test_delete_comment(self):
        self.client.login(username="user", password="pass")
        response = self.client.delete(f"/comments/{self.comment.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)
