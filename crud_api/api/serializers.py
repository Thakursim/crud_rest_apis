from rest_framework import serializers
from .models import Post

# class AuthorSerializer(serializers.ModelSerializer):
    # class Meta:
        # model = Author
        # fields = ['id', 'name', 'added_by', 'created_by']

# class BookSerializer(serializers.ModelSerializer):
    # class Meta:
        # model = Book
        # fields = ['id', 'title', 'description', 'created_date', 'author', 'added_by']
        
class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'message')        