from django.urls import path
from .views import PostListCreate, PostDetail, PostUpdate, PostDelete, CommentCreate, CommentDetail, CommentUpdate, CommentDelete

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("posts/", PostListCreate.as_view(), name="posts"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="post"),
    path("posts/<int:pk>/update/", PostUpdate.as_view(), name="post_update"),
    path("posts/<int:pk>/delete/", PostDelete.as_view(), name="post_delete"),
    path("comments/", CommentCreate.as_view(), name="comments"),
    path("comments/<int:pk>/", CommentDetail.as_view(), name="comment"),
    path("comments/<int:pk>/update/", CommentUpdate.as_view(), name="comment_update"),
    path("comments/<int:pk>/delete/", CommentDelete.as_view(), name="comment_delete"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]