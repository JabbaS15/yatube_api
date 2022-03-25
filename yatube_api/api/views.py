from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, mixins
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from posts.models import Post, Group
from .permissions import AuthorOrReadOnly, ReadOnly
from .serializers import PostSerializer, CommentSerializer, FollowSerializer, \
    GroupSerializer


class ListCreateOnlyModelViewSet(mixins.CreateModelMixin,
                                 mixins.ListModelMixin,
                                 viewsets.GenericViewSet):
    pass


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def get_permissions(self):
        if self.action == 'retrieve':
            return ReadOnly(),
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return Response(status=status.HTTP_201_CREATED)


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        return post.comments.all()

    def get_permissions(self):
        if self.action == 'retrieve':
            return ReadOnly(),
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return Response(status=status.HTTP_201_CREATED)


class FollowViewSet(ListCreateOnlyModelViewSet):
    serializer_class = FollowSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, ]
    search_fields = ['user__username', 'following__username', ]

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response(status=status.HTTP_201_CREATED)
