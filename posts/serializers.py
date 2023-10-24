from rest_framework import serializers
from .models import Post
from likes.models import Like

MAX_IMAGE_SIZE_MB = 2
MAX_DIMENSION = 4096


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    like_id = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
            "title",
            "content",
            "image",
            "is_owner",
            "profile_id",
            "profile_image",
            "like_id",
        ]

    def validate_image(self, value):
        errors = []

        if value.size > 1024 * 1024 * MAX_IMAGE_SIZE_MB:
            errors.append(f"Image size greater than {MAX_IMAGE_SIZE_MB}MB!")
        if value.image.width > MAX_DIMENSION:
            errors.append(f"Image width greater than {MAX_DIMENSION}px")
        if value.image.height > MAX_DIMENSION:
            errors.append(f"Image height greater than {MAX_DIMENSION}px")

        if errors:
            raise serializers.ValidationError(errors)

        return value

    def get_is_owner(self, obj):
        return self.context["request"].user == obj.owner

    def get_like_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            like_id = (
                Like.objects.filter(owner=user, post=obj)
                .values_list("id", flat=True)
                .first()
            )
            return like_id
        return None
