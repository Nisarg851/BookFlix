from django.shortcuts import render, redirect
from django.contrib import messages
from app.models import Category, Books, Author, Publisher, AuthorBooks, BooksPublisher, User, Offer

# Create your views here.
def home_page(request):
    return render(request, "home.html")

def signup_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        print(username)

        if password != '':

            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists!")
                return redirect('/signup/')

            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists!")
                return redirect('/signup/')

            else:
                user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password, subscription_id=0, fellow_reviewers=0, username=username)
                user.save()
                return redirect('/login/')

    return render(request, "signup_page.html")


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username, password=password).get()
        print(user)

        if user is not None:
            return redirect('/browse/')
        
        else:
            messages.info(request, 'Invalid email or Password')
            return redirect('/login/')

    return render(request, "login_page.html")

def browse_page(request):
    book_list = {}
    for category in Category.objects.all():
        books = Books.objects.filter(category=category.category_id)
        book_list[category.category_name] = list()
        if len(books) != 0:
            for book in books:
                book_list[category.category_name].append({
                    "id": book.book_id,
                    "title": book.book_title,
                    "description": book.book_description,
                    "image": book.cover_image_url,
                })
    return render(request, "browse.html", {"books": book_list})

def book_review_page(request, id):
    book = Books.objects.filter(pk=id).get()

    # Getting Authors
    authors = []
    for authbook in AuthorBooks.objects.filter(books_book=id):
        author = Author.objects.get(pk = authbook.author_author.author_id)
        authors.append("\""+author.first_name+" "+author.last_name+"\"")
    if len(authors)==0:
        authors = ["None"]

    # Getting Publishers
    publishers = []
    for bookPub in BooksPublisher.objects.filter(books_book=id):
        publisher = Publisher.objects.get(pk = bookPub.books_book.book_id)
        publishers.append("\""+publisher.publisher_name+"\" ("+publisher.email+") ")
    if len(publishers)==0:
        publishers = ["None"]

    return render(request, "book_review_page.html", {
        "book": book,
        "rating": 4, 
        "authors": authors, 
        "publishers": publishers
    })

def user_profile(request):
    context = {'current_tab': request.GET.get('current_tab')}
    return render(request, "user_profile.html", context)


def author_profile(request):
    return render(request, "author_profile.html")


def subscription(request):
    return render(request, "subscription.html")

def payment_page(request):
    return render(request, "payment_page.html")