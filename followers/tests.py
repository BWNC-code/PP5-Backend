from django.contrib.auth.models import User
from .models import Follower
from rest_framework import status
from rest_framework.test import APITestCase


class FollowerTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="pass1")
        self.user2 = User.objects.create_user(username="user2", password="pass2")

    def test_follow_user(self):
        self.client.login(username="user1", password="pass1")
        response = self.client.post("/followers/", {"followed": self.user2.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Follower.objects.count(), 1)
        self.assertTrue(
            Follower.objects.filter(owner=self.user1, followed=self.user2).exists()
        )

    def test_unfollow_user(self):
        follower = Follower.objects.create(owner=self.user1, followed=self.user2)
        self.client.login(username="user1", password="pass1")
        response = self.client.delete(f"/followers/{follower.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Follower.objects.count(), 0)

    def test_follower_count_and_retrieval(self):
        Follower.objects.create(owner=self.user1, followed=self.user2)
        self.client.login(username="user2", password="pass2")
        response = self.client.get("/followers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        followers = response.data.get("results", [])
        self.assertEqual(len(followers), 1)
        follower_usernames = [follower["owner"] for follower in followers]
        self.assertIn(self.user1.username, follower_usernames)

    def test_mutual_following(self):
        Follower.objects.create(owner=self.user1, followed=self.user2)
        Follower.objects.create(owner=self.user2, followed=self.user1)
        self.assertEqual(Follower.objects.count(), 2)
        self.assertTrue(
            Follower.objects.filter(owner=self.user1, followed=self.user2).exists()
        )
        self.assertTrue(
            Follower.objects.filter(owner=self.user2, followed=self.user1).exists()
        )
