# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Author(models.Model):
    author_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    followers = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'Author'


class AuthorBooks(models.Model):
    author_author = models.OneToOneField(Author, models.CASCADE, db_column='Author_author_id', primary_key=True)  # Field name made lowercase.
    books_book = models.ForeignKey('Books', models.CASCADE, db_column='Books_book_id')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'Author_Books'
        unique_together = (('author_author', 'books_book'),)


class Books(models.Model):
    book_id = models.IntegerField(primary_key=True)
    category = models.ForeignKey('Category', models.CASCADE)
    cover_image_url = models.CharField(max_length=255, blank=True, null=True)
    book_title = models.CharField(max_length=255)
    book_description = models.CharField(max_length=255, blank=True, null=True)
    book_softcopy_link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'Books'


class BooksPublisher(models.Model):
    books_book = models.OneToOneField(Books, models.CASCADE, db_column='Books_book_id', primary_key=True)  # Field name made lowercase.
    publisher_publisher = models.ForeignKey('Publisher', models.CASCADE, db_column='Publisher_publisher_id')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'Books_Publisher'
        unique_together = (('books_book', 'publisher_publisher'),)


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(unique=True, max_length=255)

    class Meta:
        # managed = False
        db_table = 'Category'


class Feed(models.Model):
    feed_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('User', models.CASCADE)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    upvotes = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'Feed'


class Offer(models.Model):
    offer_id = models.IntegerField(primary_key=True)
    offer_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        # managed = False
        db_table = 'Offer'


class Publisher(models.Model):
    publisher_id = models.IntegerField(primary_key=True)
    publisher_name = models.CharField(unique=True, max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        # managed = False
        db_table = 'Publisher'


class PublisherUser(models.Model):
    publisher_publisher = models.OneToOneField(Publisher, models.CASCADE, db_column='Publisher_publisher_id', primary_key=True)  # Field name made lowercase.
    user_user = models.ForeignKey('User', models.CASCADE, db_column='User_user_id')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'Publisher_User'
        unique_together = (('publisher_publisher', 'user_user'),)


class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('User', models.CASCADE)
    book = models.ForeignKey(Books, models.CASCADE)
    reviews = models.CharField(max_length=255)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'Review'


class Subscriptions(models.Model):
    subscription_id = models.IntegerField(primary_key=True)
    subscription_name = models.CharField(unique=True, max_length=255)
    duration = models.IntegerField()
    price = models.IntegerField()
    subscribers = models.IntegerField()
    offer = models.ForeignKey(Offer, models.CASCADE)

    class Meta:
        # managed = False
        db_table = 'Subscriptions'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    subscription = models.ForeignKey(Subscriptions, models.CASCADE, blank=True, null=True)
    fellow_reviewers = models.IntegerField(null=True)
    username = models.CharField(unique=True, max_length=255)

    class Meta:
        # managed = False
        db_table = 'User'


class UserAuthor(models.Model):
    user_user = models.OneToOneField(User, models.CASCADE, db_column='User_user_id', primary_key=True)  # Field name made lowercase.
    author_author = models.ForeignKey(Author, models.CASCADE, db_column='Author_author_id')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'User_Author'
        unique_together = (('user_user', 'author_author'),)


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         # managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.CASCADE)
#     permission = models.ForeignKey('AuthPermission', models.CASCADE)

#     class Meta:
#         # managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.CASCADE)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         # managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         # managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.CASCADE)
#     group = models.ForeignKey(AuthGroup, models.CASCADE)

#     class Meta:
#         # managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.CASCADE)
#     permission = models.ForeignKey(AuthPermission, models.CASCADE)

#     class Meta:
#         # managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.CASCADE, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.CASCADE)

#     class Meta:
#         # managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         # managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         # managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         # managed = False
#         db_table = 'django_session'
