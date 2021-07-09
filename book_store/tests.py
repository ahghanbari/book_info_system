
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from .models import Book


class BookTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.book = Book.objects.create(
            title='foo',
            pub_date='2021-11-20',
            pages_number=2001,
            price=200,
            description='Nice description',
            author=self.user,
        )
        
    def test_string_representation(self):
        book = Book(title='foo')
        self.assertEqual(str(book), book.title)

    def test_book_content(self):
        self.assertEqual(f'{self.book.title}', 'foo')
        self.assertEqual(f'{self.book.author}', 'testuser')
        self.assertEqual(f'{self.book.pub_date}', '2021-11-20')
        self.assertEqual(f'{self.book.pages_number}', '2001')
        self.assertEqual(f'{self.book.price}', '200')
        self.assertEqual(f'{self.book.description}', 'Nice description')
        

    def test_book_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice description')
        self.assertContains(response, 'foo')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_book_detail_view(self):
        response = self.client.get('/book/1/')
        no_response = self.client.get('/book/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'foo')
        self.assertTemplateUsed(response, 'book_detail.html')

    def test_book_create_view(self):
        response = self.client.post(reverse('book_new'), {
            'title': 'New title',
            'pub_date': '2021-11-21',
            'price': '220',
            'pages_number': '5000',
            'description': 'New text',
            'author': self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')
        self.assertContains(response, '5000')
        self.assertContains(response, '220')

    def test_book_update_view(self):
        response = self.client.post(reverse('book_edit', args='1'), {
            'title': 'Updated title',
            'pub_date': '2021-11-21',
            'pages_number': '5000',
            'price': '221',
            'description': 'Updated text',
        })
        self.assertEqual(response.status_code, 302)
    
    def test_book_delete_view(self):
        response = self.client.get(
            reverse('book_delete', args='1')
        )
        self.assertEqual(response.status_code, 200)