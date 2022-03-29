from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CurrentUserDefault
from rest_framework.generics import get_object_or_404
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Group, Post, Comment, Follow, User


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для постов"""
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для коментариев"""
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для групп"""
    class Meta:
        model = Group
        fields = "__all__"


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для папещиков"""
    user = SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=CurrentUserDefault()
    )
    following = SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    def validate_following(self, value):
        """Валидатор поля validate_following"""
        following = get_object_or_404(User, username=value)
        user = self.context['request'].user
        if user == following:
            raise ValidationError('Вы не можете подписаться на самого себя!')
        return value

    class Meta:
        model = Follow
        exclude = ['id']
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Нельзя подписаться на автора повторно!'
            )
        ]
