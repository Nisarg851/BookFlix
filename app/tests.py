from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from app.models import User, Category, Books, Author, AuthorBooks, Publisher, BooksPublisher

class HomePageViewTest(TestCase):
    def test_home_page_loads(self):
        client = Client()
        response = client.get(reverse('home_page'))  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class SignupPageViewTest(TestCase):
    def test_signup_page_loads(self):
        client = Client()
        response = client.get(reverse('signup_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup_page.html')

    def test_signup_successful(self):
        client = Client()
        data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password': 'testpassword',
        }
        response = client.post(reverse('signup_page'), data)
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.get(username='testuser')
        self.assertEqual(user.email, 'test@example.com')

    def test_signup_existing_email(self):
        User.objects.create(username='existinguser', email='test@example.com', password='password')
        client = Client()
        data = {
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'test@example.com',
            'password': 'newpassword',
        }
        response = client.post(reverse('signup_page'), data)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Email already exists!")

    def test_signup_existing_username(self):
        User.objects.create(username='testuser', email='existing@example.com', password='password')
        client = Client()
        data = {
            'username': 'testuser',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'new@example.com',
            'password': 'newpassword',
        }
        response = client.post(reverse('signup_page'), data)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Username already exists!")

    def test_signup_empty_password(self):
        client = Client()
        data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password': '',
        }
        response = client.post(reverse('signup_page'), data)
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(User.objects.count(), 0) 

class LoginPageViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpassword', email="test@test.com", first_name='test', last_name='test')

    def test_login_page_loads(self):
        client = Client()
        response = client.get(reverse('login_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login_page.html')

    def test_login_successful(self):
        client = Client()
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = client.post(reverse('login_page'), data)
        self.assertEqual(response.status_code, 302)  

    def test_login_invalid_credentials(self):
        client = Client()
        data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = client.post(reverse('login_page'), data)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Invalid email or Password")

class BrowsePageViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(category_id=1, category_name='Fiction')
        self.book = Books.objects.create(book_id=1, category=self.category, book_title='Test Book', book_description='Description')

    def test_browse_page_loads(self):
        client = Client()
        response = client.get(reverse('browse_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'browse.html')
        self.assertIn('books', response.context)
        self.assertIn('Fiction', response.context['books'])
        self.assertEqual(len(response.context['books']['Fiction']), 1)
        self.assertEqual(response.context['books']['Fiction'][0]['title'], 'Test Book')

class BookReviewPageViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(category_id=1, category_name='Fiction')
        self.book = Books.objects.create(book_id=1, category=self.category, book_title='Test Book', book_description='Description')
        self.author = Author.objects.create(author_id=1, first_name='Test', last_name='Author', followers=0)
        self.author_book = AuthorBooks.objects.create(author_author_id=1, books_book_id=1)
        self.publisher = Publisher.objects.create(publisher_id=1, publisher_name='Test Publisher', email='test@publisher.com')
        self.book_publisher = BooksPublisher.objects.create(books_book_id=1, publisher_publisher_id=1)

    def test_book_review_page_loads(self):
        client = Client()
        response = client.get(reverse('book_review', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_review_page.html')
        self.assertIn('book', response.context)
        self.assertIn('authors', response.context)
        self.assertIn('publishers', response.context)
        self.assertEqual(response.context['authors'][0], '"Test Author"')
        self.assertEqual(response.context['publishers'])