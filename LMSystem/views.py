from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from rest_framework .generics import GenericAPIView
from rest_framework import status
from rest_framework .response import Response

from.serializers import CategorySerializer
from.serializers import AuthorsSerializer
from.serializers import BookSerializer
from.serializers import BookFileSerializer

from.models import Category
from.models import Authors
from.models import Book
from.models import BookFile

# Create your views here.
class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AuthorsView(ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer

class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookFileView(GenericAPIView):
    queryset = BookFile.objects.all()
    serializer_class = BookFileSerializer

    def get(self,request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)    
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

class BookFileViewDetail(GenericAPIView):
    queryset = BookFile.objects.all()
    serializer_class = BookFileSerializer

    def get(self,request,pk):
        try:
            bookfile_obj =BookFile.objects.get(fileID=pk)
        except:
            return Response('file not found',status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(bookfile_obj)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            bookfile_obj =BookFile.objects.get(fileID=pk)
        except:
            return Response('file not found',status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(bookfile_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            bookfile_obj =BookFile.objects.get(fileID=pk)
        except:
            return Response('file not found',status=status.HTTP_404_NOT_FOUND)
        bookfile_obj.delete()
        return Response('file deleted',status=status.HTTP_204_NO_CONTENT)





    