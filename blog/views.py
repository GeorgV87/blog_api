from rest_framework import generics, permissions
from .models import Post, Comment
from .serializer import PostSerializer, CommentSerializer

# Create your views here.
class PostListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class PostDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
    
class PostUpdate(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
        
class PostDelete(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class CommentCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class CommentDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class CommentUpdate(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
        
class CommentDelete(generics.DestroyAPIView):  
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)