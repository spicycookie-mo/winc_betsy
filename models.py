# Models go here
import peewee
import datetime

"""In SQLite, foreign keys are not enabled by default. 
Most things, including the Peewee foreign-key API, will work fine, 
but ON DELETE behaviour will be ignored, even if you explicitly specify on_delete in your ForeignKeyField. 
In conjunction with the default AutoField behaviour (where deleted record IDs can be reused), 
this can lead to subtle bugs. 
To avoid problems, I recommend that you enable foreign-key constraints when using SQLite, 
by setting pragmas={'foreign_keys': 1} when you instantiate SqliteDatabase."""

db = peewee.SqliteDatabase("betsy.db", pragmas={'foreign_keys': 1})

class User(peewee.Model):
    name = peewee.CharField(max_length=50)
    e_mail = peewee.CharField(unique=True)

    class Meta:
        database = db

class Address(peewee.Model):
    user = peewee.ForeignKeyField(User, backref='addresses', on_delete='CASCADE')
    country = peewee.CharField()
    state = peewee.CharField(null=True)
    city = peewee.CharField()
    street = peewee.CharField()
    street_number = peewee.CharField()
    apartment_number = peewee.IntegerField(null=True)
    zip_code = peewee.CharField()
    notes = peewee.CharField(null=True)
    is_active = peewee.BooleanField()

    class Meta:
        database = db

class PaymentInfo(peewee.Model):
    user = peewee.ForeignKeyField(User, backref='payment_info', on_delete='CASCADE')
    card_number = peewee.CharField()
    expiration_date = peewee.CharField()
    cvv = peewee.CharField()
    is_active = peewee.BooleanField()

    class Meta:
        database = db

class Tag(peewee.Model):
    name = peewee.CharField(unique=True, max_length=50)

    class Meta:
        database = db


"""BONUS: Additionally the products should be indexed so that the time spent on querying them is minimized."""
class Product(peewee.Model):
    seller = peewee.ForeignKeyField(User, backref='products', on_delete='CASCADE')
    name = peewee.CharField(max_length=50)
    description = peewee.TextField()
    price_in_cents = peewee.IntegerField()
    quantity = peewee.IntegerField()
    tags = peewee.ManyToManyField(Tag)

    class Meta:
        database = db
        # Multi-column indexes may be defined as Meta attributes using a nested tuple. 
        # Each database index is a 2-tuple, the first part of which is a tuple of the names of the fields, 
        # the second part a boolean indicating whether the index should be unique
        indexes = (
            (('name','description'), True), #Remember to add a trailing comma if your tuple of indexes contains only one item
        )

    def __str__(self):
        return self.name

class Transaction(peewee.Model):
    buyer = peewee.ForeignKeyField(User, backref='transactions', null=False, on_delete='CASCADE')
    product = peewee.ForeignKeyField(Product, backref='transactions', null=False, on_delete='CASCADE')
    quantity = peewee.IntegerField()
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

# Get a reference to the automatically-created through table.
ProductTag = Product.tags.get_through_model()

# Create tables for our two models as well as the through model.
db.create_tables([User, Address, PaymentInfo, Tag, Product, Transaction, ProductTag])