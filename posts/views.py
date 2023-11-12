from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from travel_social.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count("comment", distinct=True),
        likes_count=Count("likes", distinct=True),
    ).order_by("-created_at")
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "owner__followed__owner__profile",  # Posts of users followed by the current user
        "likes__owner__profile",  # Posts liked by the current user
        "owner__profile",  # Posts of the current user
        "category",
    ]
    search_fields = [
        "owner__username",
        "title",
    ]
    ordering_fields = [
        "comments_count",
        "likes_count",
        "likes__created_at",
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count("comment", distinct=True),
        likes_count=Count("likes", distinct=True),
    ).order_by("-created_at")
