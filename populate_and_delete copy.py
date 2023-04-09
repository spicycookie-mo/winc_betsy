from models import User, Address, PaymentInfo, Tag, Product, Transaction, ProductTag, db
import peewee


def populate_test_database():

    # Create users
    users = [
        {'name': 'Alice', 'e_mail': 'alice@example.com'},
        {'name': 'Bob', 'e_mail': 'bob@example.com'},
        {'name': 'Alex', 'e_mail': 'alex@example.com'}
    ]

    with db.atomic():
        User.insert_many(users).execute()

        # Create addresses
        addresses = [
            {'user_id': 1, 'country': 'Romania', 'city': 'Bucharest', 'street': 'Brezoianu', 'street_number': '51', 'zip_code': '000000', 'is_active': True},
            {'user_id': 2, 'country': 'Russia', 'city': 'Saint Petersburg', 'street': 'Nevsky Prospekt', 'street_number': '456', 'apartment_number': '12B', 'zip_code': '999999', 'is_active': True},
            {'user_id': 3, 'country': 'UK', 'city': 'London', 'street': 'Oxford Street', 'street_number': '789', 'zip_code': '123456', 'is_active': True},
        ]
        Address.insert_many(addresses).execute()

        # Create payment info
        payment_infos = [
            {'user_id': 1, 'card_number': '1234567890123456', 'expiration_date': '12/23', 'cvv': '123', 'is_active': True},
            {'user_id': 2, 'card_number': '1111222233334444', 'expiration_date': '11/22', 'cvv': '456', 'is_active': True},
            {'user_id': 3, 'card_number': '5555666677778888', 'expiration_date': '10/25', 'cvv': '789', 'is_active': True},
        ]
        PaymentInfo.insert_many(payment_infos).execute()

    # Create tags
    # Create tags
    jewelry = Tag.create(name='jewelry')
    jewelry.save()
    clothing = Tag.create(name='clothing')
    clothing.save()
    home = Tag.create(name='home')
    art = Tag.create(name='art')
    vintage = Tag.create(name='vintage')

    # Create products
    products = [
        {'seller': 2, 'name': 'Cozy Sweater', 'description': 'A warm and cozy sweater to keep you warm during the winter months', 'price_in_cents': 2999, 'quantity': 5, 'tags': [clothing]},
        {'seller': 1, 'name': 'Boho Beaded Necklace', 'description': 'Handmade necklace with colorful beads and tassel', 'price_in_cents': 2999, 'quantity': 10, 'tags': [jewelry]},
        {'seller': 1, 'name': 'Macrame Wall Hanging', 'description': 'Large wall hanging with intricate knotwork', 'price_in_cents': 4999, 'quantity': 5, 'tags': [home, art]},
        {'seller': 1, 'name': 'Knitted Infinity Scarf', 'description': 'Soft and warm scarf in earthy tones', 'price_in_cents': 3999, 'quantity': 7, 'tags': [clothing]},
        {'seller': 1, 'name': 'Hand-Poured Soy Candle', 'description': 'Eco-friendly candle in a reusable jar', 'price_in_cents': 1999, 'quantity': 20, 'tags': [home]},
        {'seller': 2, 'name': 'Embroidered Hoop Art', 'description': 'Cute and colorful wall decor', 'price_in_cents': 2499, 'quantity': 15, 'tags': [home, art]},
        {'seller': 2, 'name': 'Crochet Baby Blanket', 'description': 'Soft and cozy blanket for newborns', 'price_in_cents': 5999, 'quantity': 3, 'tags': [home]},
        {'seller': 2, 'name': 'Handmade Ceramic Mug', 'description': 'Beautiful mug with unique glaze', 'price_in_cents': 2499, 'quantity': 12, 'tags': [home]},
        {'seller': 3, 'name': 'Embroidered Denim Jacket', 'description': 'One-of-a-kind jacket with floral embroidery', 'price_in_cents': 8999, 'quantity': 2, 'tags': [clothing]},
        {'seller': 3, 'name': 'Vintage Leather Jacket', 'description': 'A classic vintage leather jacket from the 80s', 'price_in_cents': 8000, 'quantity': 1, 'tags': [clothing, vintage]},
        {'seller': 3, 'name': 'Hand-painted watercolor portrait', 'description': 'A beautiful, custom hand-painted watercolor portrait of a person or pet. Perfect as a gift or to add a personal touch to your home decor.', 'price_in_cents': 2499, 'quantity': 1, 'tags': [art]}
    ]
    #  products = [
    #     {'seller': User.get(User.name == 'Bob'), 'name': 'Cozy Sweater', 'description': 'A warm and cozy sweater to keep you warm during the winter months', 'price_in_cents': 2999, 'quantity': 5, 'tags': [clothing]},
    #     {'seller': User.get(User.name == 'Alice'), 'name': 'Boho Beaded Necklace', 'description': 'Handmade necklace with colorful beads and tassel', 'price_in_cents': 2999, 'quantity': 10, 'tags': [jewelry]},
    #     {'seller': User.get(User.name == 'Alice'), 'name': 'Macrame Wall Hanging', 'description': 'Large wall hanging with intricate knotwork', 'price_in_cents': 4999, 'quantity': 5, 'tags': [home, art]},
    #     {'seller': User.get(User.name == 'Alice'), 'name': 'Knitted Infinity Scarf', 'description': 'Soft and warm scarf in earthy tones', 'price_in_cents': 3999, 'quantity': 7, 'tags': [clothing]},
    #     {'seller': User.get(User.name == 'Alice'), 'name': 'Hand-Poured Soy Candle', 'description': 'Eco-friendly candle in a reusable jar', 'price_in_cents': 1999, 'quantity': 20, 'tags': [home]},
    #     {'seller': User.get(User.name == 'Bob'), 'name': 'Embroidered Hoop Art', 'description': 'Cute and colorful wall decor', 'price_in_cents': 2499, 'quantity': 15, 'tags': [home, art]},
    #     {'seller': User.get(User.name == 'Bob'), 'name': 'Crochet Baby Blanket', 'description': 'Soft and cozy blanket for newborns', 'price_in_cents': 5999, 'quantity': 3, 'tags': [home]},
    #     {'seller': User.get(User.name == 'Bob'), 'name': 'Handmade Ceramic Mug', 'description': 'Beautiful mug with unique glaze', 'price_in_cents': 2499, 'quantity': 12, 'tags': [home]},
    #     {'seller': User.get(User.name == 'Alex'), 'name': 'Embroidered Denim Jacket', 'description': 'One-of-a-kind jacket with floral embroidery', 'price_in_cents': 8999, 'quantity': 2, 'tags': [clothing]},
    #     {'seller': User.get(User.name == 'Alex'), 'name': 'Vintage Leather Jacket', 'description': 'A classic vintage leather jacket from the 80s', 'price_in_cents': 8000, 'quantity': 1, 'tags': [clothing, vintage]},
    #     {'seller': User.get(User.name == 'Alex'), 'name': 'Hand-painted watercolor portrait', 'description': 'A beautiful, custom hand-painted watercolor portrait of a person or pet. Perfect as a gift or to add a personal touch to your home decor.', 'price_in_cents': 2499, 'quantity': 1, 'tags': [art]}
    # ]

    for product in products:
        tags = product.pop('tags')
        new_product = Product.create(**product)
        new_product.tags.add(tags)
        new_product.save()

populate_test_database()


def delete_test_data():
# first need to delete the through table, else foreign key error
    ProductTag.delete().execute()
    Transaction.delete().execute()
    Product.delete().execute()
    Tag.delete().execute()
    PaymentInfo.delete().execute()
    Address.delete().execute()
    User.delete().execute()

# delete_test_data()

