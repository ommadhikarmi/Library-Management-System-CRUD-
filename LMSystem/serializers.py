from rest_framework import serializers
from .models import Category
from .models import Authors
from .models import Book
from .models import BookFile



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__' 

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookFile
        fields = '__all__'
    