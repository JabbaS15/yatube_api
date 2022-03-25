from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

from posts.models import User, Follow


def validate_following(self, value):
    following = get_object_or_404(User, username=value)
    user = self.context['request'].user
    author_filters = Follow.objects.filter(following=following, user=user)
    if user == following:
        raise ValidationError(
            'Вы не можете подписаться на самого себя!')
    elif author_filters:
        raise ValidationError(
            'Вы уже подписаны')
    return value
