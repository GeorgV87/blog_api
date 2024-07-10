from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    content = serializers.StringRelatedField()
    
    class Meta:
        model = Post
        fields = '__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    post = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    content = serializers.StringRelatedField()
    
    class Meta:
        model = Comment
        fields = '__all__'