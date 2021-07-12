from peewee import * 
from models import *

# create database with dummy data
def create_database():
    db.create_tables([Users, Products, Tags, User_products, Product_tags, Transactions])

    # create users
    sjaan = Users.create(name='Sjaan Bovenkamp', adress='Achterkamp 66', billing_info='Sjaan Bovenkamp, Achterkamp 66, 1900 AA, Urk')
    willeke = Users.create(name='Willeke Alberti', adress='Hoog varen 22', billing_info='Willeke Alberti, Hoog varen 22, 1901 AB, Groningen')
    freddy = Users.create(name='Freddy de Boer', adress='Dorpstraat 27', billing_info='freddy freddysen, Dorpstraat 27, 1902 BB, Geldermalsen')
    bertje = Users.create(name='Bertje Bobson', adress='Lange dreef 21', billing_info='Bertje Bobson, Lange dreef 21, 1902 BB, Volendam')

    # create products
    hot_sauce = Products.create(name='Hot sauce', description='Heet, heter, heetst', price=1.20, quantity=87)
    mayonnaise = Products.create(name='Mayonnaise', description='Wajoo, vette mayo', price=0.80, quantity=53)
    mustard = Products.create(name='Mustard', description='Na de maaltijd', price=2.10, quantity=34)
    garlic_sauce = Products.create(name='Garlic sauce', description='Stink er niet in', price=1.10, quantity=53)
    joppie_sauce = Products.create(name='Joppie sauce', description='Helemaal Toppie', price=1.80, quantity=43)
    jambala_sauce = Products.create(name='Jambala', description='Jambala-la-la', price=1.40, quantity=34)

    # create tags
    spicy = Tags.create(name='Spicy')
    fat = Tags.create(name='Fat')
    fresh = Tags.create(name='Fresh')
    spices = Tags.create(name='Spices')
    sharp = Tags.create(name='Sharp')
    sweet = Tags.create(name='Sweet')

    # create user products
    User_products.create(user=sjaan, product=hot_sauce, quantity=123)
    User_products.create(user=willeke, product=mayonnaise, quantity=89)
    User_products.create(user=willeke, product=mustard, quantity=75)
    User_products.create(user=freddy, product=garlic_sauce, quantity=96)
    User_products.create(user=freddy, product=mayonnaise, quantity=194)
    User_products.create(user=freddy, product=joppie_sauce, quantity=175)
    User_products.create(user=bertje, product=jambala_sauce, quantity=210)

    # create tags linked to products
    Product_tags.create(product=hot_sauce, tag=spicy)
    Product_tags.create(product=hot_sauce, tag=sharp)
    Product_tags.create(product=mayonnaise, tag=fat)
    Product_tags.create(product=mustard, tag=sharp)
    Product_tags.create(product=garlic_sauce, tag=fresh)
    Product_tags.create(product=joppie_sauce, tag=fat)
    Product_tags.create(product=jambala_sauce, tags=spicy)
    Product_tags.create(product=jambala_sauce, tags=spices)
    Product_tags.create(product=jambala_sauce, tags=sweet)
