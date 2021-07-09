from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'home.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_new.html'
    #fields = ['title', 'pub_date', 'pages_number', 'price', 'description']
    fields = '__all__'

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_edit.html'
    fields = ['title', 'pub_date', 'pages_number', 'price', 'description']


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('home')