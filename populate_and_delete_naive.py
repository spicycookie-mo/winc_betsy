from models import User, Address, PaymentInfo, Tag, Product, Transaction, ProductTag, db
import peewee


def populate_test_database():

    # Create users
    alice = User.create(name='Alice', e_mail='alice@example.com')
    bob = User.create(name='Bob', e_mail='bob@example.com')
    alex = User.create(name='Alex', e_mail='alex@example.com')
    
    # Create addresses
    alice_address = Address.create(user=alice, country='Romania', city='Bucharest', street='Brezoianu', street_number='51', zip_code='000000', is_active=True)
    bob_address = Address.create(user=bob, country='Russia', city='Saint Petersburg', street='Nevsky Prospekt', street_number='456', apartment_number='12B', zip_code='999999', is_active=True)
    alex_address = Address.create(user=alex, country='UK', city='London', street='Oxford Street', street_number='789', zip_code='123456', is_active=True)
    
    # Create payment info
    alice_payment_info = PaymentInfo.create(user=alice, card_number='1234567890123456', expiration_date='12/23', cvv='123', is_active=True)
    bob_payment_info = PaymentInfo.create(user=bob, card_number='1111222233334444', expiration_date='11/22', cvv='456', is_active=True)
    charlie_payment_info = PaymentInfo.create(user=alex, card_number='5555666677778888', expiration_date='10/25', cvv='789', is_active=True)

    # Create tags
    jewelry = Tag.create(name='jewelry')
    clothing = Tag.create(name='clothing')
    home = Tag.create(name='home')
    art = Tag.create(name='art')
    vintage = Tag.create(name='vintage')


    # Create products
    product0 = Product.create(seller=bob, name='Cozy Sweater', description='A warm and cozy sweater to keep you warm during the winter months', price_in_cents=2999, quantity=5)
    product0.tags.add([clothing])

    product1 = Product.create(seller=alice, name='Boho Beaded Necklace', description='Handmade necklace with colorful beads and tassel', price_in_cents=2999, quantity=10)
    product1.tags.add([jewelry])

    product2 = Product.create(seller=alice, name='Macrame Wall Hanging', description='Large wall hanging with intricate knotwork', price_in_cents=4999, quantity=5)
    product2.tags.add([home, art])

    product3 = Product.create(seller=alice, name='Knitted Infinity Scarf', description='Soft and warm scarf in earthy tones', price_in_cents=3999, quantity=7)
    product3.tags.add([clothing])

    product4 = Product.create(seller=alice, name='Hand-Poured Soy Candle', description='Eco-friendly candle in a reusable jar', price_in_cents=1999, quantity=20)
    product4.tags.add([home])

    product5 = Product.create(seller=bob, name='Embroidered Hoop Art', description='Cute and colorful wall decor', price_in_cents=2499, quantity=15)
    product5.tags.add([home, art])

    product6 = Product.create(seller=bob, name='Crochet Baby Blanket', description='Soft and cozy blanket for newborns', price_in_cents=5999, quantity=3)
    product6.tags.add([home])

    product7 = Product.create(seller=bob, name='Handmade Ceramic Mug', description='Beautiful mug with unique glaze', price_in_cents=2499, quantity=12)
    product7.tags.add([home])

    product8 = Product.create(seller=alex, name='Embroidered Denim Jacket', description='One-of-a-kind jacket with floral embroidery', price_in_cents=8999, quantity=2)
    product8.tags.add([clothing])

    product9 = Product.create(seller=alex, name="Vintage Leather Jacket", description="A classic vintage leather jacket from the 80s", price_in_cents=8000, quantity=1)
    product9.tags.add([clothing, vintage])

    product10 = Product.create(seller=alice, name="Hand-painted watercolor portrait", description="A beautiful, custom hand-painted watercolor portrait of a person or pet. Perfect as a gift or to add a personal touch to your home decor.",
    price_in_cents=2499, quantity=1)
    product10.tags.add([art])

populate_test_database()


def delete_test_data():
# first need to delete the through table, else i get foreign key error
    ProductTag.delete().execute()
    Transaction.delete().execute()
    Product.delete().execute()
    Tag.delete().execute()
    PaymentInfo.delete().execute()
    Address.delete().execute()
    User.delete().execute()

# delete_test_data()

