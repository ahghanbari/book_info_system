
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.full_name', read_only=True)
    class Meta:
        model = Book
        fields = ['title', 'author', 'pub_date', 'pages_number', 'price', 'description']
