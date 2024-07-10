from django.urls import path
from .views import PostListCreate, PostDetail, CommentCreate, CommentDetail

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("posts/", PostListCreate.as_view(), name="posts"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="post"),
    path("comments/", CommentCreate.as_view(), name="comments"),
    path("comments/<int:pk>/", CommentDetail.as_view(), name="comment"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]