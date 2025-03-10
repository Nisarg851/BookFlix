from django.contrib import admin
from .models import Author, Category, Books, Publisher, Offer, Subscriptions, User, Review, Feed, UserAuthor, PublisherUser, BooksPublisher, AuthorBooks

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Books)
admin.site.register(Publisher)
admin.site.register(Offer)
admin.site.register(Subscriptions)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(Feed)
admin.site.register(UserAuthor)
admin.site.register(PublisherUser)
admin.site.register(BooksPublisher)
admin.site.register(AuthorBooks)


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'home.html', {'author': authors})