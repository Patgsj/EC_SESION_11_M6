from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'catalog/book_list.html', {'books': books})
def boards(request):
    return render(request, 'catalog/boards.html')

# Create your views here.
