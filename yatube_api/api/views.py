from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, mixins
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from posts.models import Post, Group
from .permissions import AuthorOrReadOnly
from .serializers import PostSerializer, CommentSerializer, FollowSerializer, \
    GroupSerializer


class ListCreateOnlyModelViewSet(mixins.CreateModelMixin,
                                 mixins.ListModelMixin,
                                 viewsets.GenericViewSet):
    """A viewset that provides, `create`, and `list` actions."""
    pass


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Работает с группами, только чтение."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)


class PostViewSet(viewsets.ModelViewSet):
    """Работает с постами пользователей."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return Response(status=status.HTTP_201_CREATED)


class CommentsViewSet(viewsets.ModelViewSet):
    """Работает с комментариями пользователей."""
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return Response(status=status.HTTP_201_CREATED)


class FollowViewSet(ListCreateOnlyModelViewSet):
    """Возвращает из БД и создает подписки пользователя"""
    permission_classes = (IsAuthenticated,)
    serializer_class = FollowSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, ]
    search_fields = ['user__username', 'following__username', ]

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response(status=status.HTTP_201_CREATED)
