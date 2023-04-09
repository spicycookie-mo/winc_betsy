__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import User, Address, PaymentInfo, Tag, Product, Transaction, ProductTag, db
# import models
from peewee import fn
from spellchecker import SpellChecker

spell = SpellChecker() # loads default word frequency list


def search(term) -> list[Product]:
    """"Search for products based on a term. 
    Searching for 'sweater' should yield all products that have the word 'sweater' in the name. 
    This search should be case-insensitive.
    Bonus: The search should target both the name and description fields.
    Bonus: The search should account for spelling mistakes made by users and return products even if a spelling error is present
    http://norvig.com/spell-correct.html
    https://pypi.org/project/pyspellchecker/
    https://pyspellchecker.readthedocs.io/en/latest/
    """
    
    # corrected_term = spell.correction(term)    ###works for one word only
    corrected_term = ' '.join([spell.correction(word) for word in term.split()])
    # print(corrected_term)
    
    query = (Product
             .select(Product.name)
             .where(fn.lower(Product.name).contains(corrected_term.lower()) | fn.lower(Product.description).contains(corrected_term.lower())))
    return list(query)

print(f'Showing results for "sweater": {search("sweater")}')
print(f'Showing results for "jacket": {search("jacket")}')
print(f'Showing results for "wall": {search("wall")}') # returns id 5 too, after adding description field too search
print(f'Showing results for "sweather": {search("sweather")}') # oops expected to correct term to 'sweater' (delete assert) but doesn't...
print(f'Showing results for "sweatter": {search("sweatter")}') # corrects term to 'sweater' (delete assert)
print(f'Showing results for "sweter": {search("sweter")}') # corrects term to 'sweater' (insert assert)
print(f'Showing results for "cozi sweter": {search("cozi sweter")}') # corrects term to 'sweater' (replace + insert assert)



def list_user_products(user_id) -> list[Product]:
    """View the products of a given user."""
    query = (Product
             .select(Product)
             .join(User) 
             .where(Product.seller_id == user_id))
    return list(query)

print(f'Product(s) offered by Alice: {list_user_products(1)}')
print(f'Product(s) offered by Bob: {list_user_products(2)}')
print(f'Product(s) offered by Alex: {list_user_products(3)}')



def list_products_per_tag(tag_id) -> list[Product]:
    """"View all products for a given tag."""
    query = (Product
             .select(Product)
             .join(ProductTag)
             .where(ProductTag.tag_id == tag_id))
    return list(query)

print(f'Product(s) linked to Jewelry tag: {list_products_per_tag(1)}')
print(f'Product(s) linked to Clothing tag 1: {list_products_per_tag(2)}')
print(f'Product(s) linked to Home tag 1: {list_products_per_tag(3)}')
print(f'Product(s) linked to Art tag 1: {list_products_per_tag(4)}')
print(f'Product(s) linked to Vintage tag 1: {list_products_per_tag(5)}')



def add_product_to_catalog(user_id, product) -> Product:
    """Add a product to a user."""
    # type(product) = dict

    # if product already exists, then quantity incremented, else new product added
    # Get the existing product, or create a new one with the given defaults.
   
    new_product, created_product = Product.get_or_create(
        seller_id = user_id,
        name = product.get('name'),
        description = product.get('description'),
        price_in_cents = product.get('price_in_cents'),
        # Any keyword argument passed to get_or_create() will be used in the get() portion of the logic, 
        # except for the defaults dictionary, which will be used to populate values on newly-created instances.
        defaults={'quantity': product.get('quantity')})
    
    # If the product already existed, increment its quantity.
    if not created_product:
        new_product.quantity += new_product.quantity + product.get('quantity')
        new_product.save()        
    # If product is new, update the through table
    else:
        Product.get(Product.name == product.get('name')).tags.add(Tag.select().where(Tag.name.in_(list(product.get('tags')))))

    return new_product

print(f"New product added to catalog: {add_product_to_catalog(2,{'name':'Flower earings', 'description':'Lovely handmade retro flower stud earrings','price_in_cents':2499, 'quantity':1, 'tags':['jewelry']})}")



def update_stock(product_id, new_quantity) -> Product:
    """"Update the stock quantity of a product."""
    product = Product.select().where(Product.id == product_id).get()
    product.quantity = new_quantity
    product.save()
    return product

print(f'Updated stock for {update_stock(11,1)}')


def remove_product(product_id):
    """Remove a product from a user."""
    product = Product.select().where(Product.id == product_id).get()
    ProductTag.delete().where(ProductTag.product_id == product_id).execute()
    # Product.delete().where(Product.id == product_id).execute()
    product.delete_instance()
    return product
    
# print(f'Product removed: {remove_product(10)}')


def purchase_product(product_id, buyer_id, quantity):
    query = Transaction.create(buyer_id = buyer_id,
                       product_id = product_id,
                        quantity = quantity)
    
    product = Product.select().where(Product.id == product_id).get() 
    new_quantity = product.quantity - quantity
    # print(new_quantity)
    update_stock(product_id, new_quantity)
    return query

print(purchase_product(4, 3, 2))
    





