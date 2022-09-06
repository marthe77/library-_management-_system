from rest_framework import generics

from Books.models import Books
from .serializers import BooksSerializer


class BookAPIView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer