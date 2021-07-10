#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


 
class BookListView(ListView):
    model = Book
    template_name = 'home.html'

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'book_detail.html'
    login_url = 'login'


class BookCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = '/login/'
    model = Book
    template_name = 'book_new.html'
    #fields = ['title', 'pub_date', 'pages_number', 'price', 'description']
    fields = '__all__'
    login_url = 'login'
   
class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'book_edit.html'
    fields = ['title', 'pub_date', 'pages_number', 'price', 'description']
    login_url = 'login'


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

class PublicBookList(APIView):
    def get(self, request):
        msgs = Book.objects.all()
        data = BookSerializer(msgs, many=True).data
        return Response(data)