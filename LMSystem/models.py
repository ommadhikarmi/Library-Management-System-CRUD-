from django.db import models

# Create your models here.

class Category(models.Model):
    bookID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

class Authors(models.Model):
    bookID = models.AutoField(primary_key=True)
    name =models.CharField(max_length=100)
    biography = models.TextField(blank=True)

class Book(models.Model):
    bookID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Authors,related_name='books')
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, related_name='books')
    edition = models.CharField(max_length=100)
    publication_year = models.IntegerField()    

class BookFile(models.Model):
    PDF = 'pdf'
    MOBI = 'mobi'
    EPUB = 'epub'
    TXT = 'txt'

    FORMAT_CHOICES = [
        (PDF, 'PDF'),
        (MOBI, 'MOBI'),
        (EPUB, 'EPUB'),
        (TXT, 'TXT'),
    ]
    fileID =  models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='files')
    # on_delete=models.CASCADE --> specifying that if the referenced object is deleted, the related objects should also be deleted
    # related_name--> providing a name to access related objects from the opposite side of the relationship. 
    format = models.CharField(max_length=100,choices=FORMAT_CHOICES)
    filepath = models.FileField(upload_to='books/',max_length=255,null=True,default=None)



    
    