from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Author, Book, Order, OrderItem

class BookstoreTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(name='Test Author', biography='Bio of test author')
        self.book = Book.objects.create(title='Test Book', isbn='1234567890123', price=10.99, stock_quantity=5, author=self.author)
        self.order = Order.objects.create(user=self.user)
        self.order_item = OrderItem.objects.create(order=self.order, book=self.book, quantity=2)

    def test_book_creation(self):
        self.assertEqual(Book.objects.count(), 1)

    def test_author_creation(self):
        self.assertEqual(Author.objects.count(), 1)

    def test_order_creation(self):
        self.assertEqual(Order.objects.count(), 1)

    def test_order_item_creation(self):
        self.assertEqual(OrderItem.objects.count(), 1)

    def test_inventory_stock_level(self):
        self.assertEqual(self.book.stock_quantity, 5)

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
