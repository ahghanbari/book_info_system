from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'home.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'