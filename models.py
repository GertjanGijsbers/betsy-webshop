from peewee import *

db = SqliteDatabase("webshop.db")

class BaseModel(Model):
    class Meta:
        database = db

class Users(BaseModel):
    name = CharField(primary_key=True, index=True)
    adress = CharField()
    billing_info = TextField()

class Products(BaseModel):
    name = CharField(unique=True, index=True)
    description = TextField()
    price = DecimalField(decimal_places=2)
    quantity = IntegerField()

class Tags(BaseModel):
    name = CharField(unique=True)

class User_products(BaseModel):
    user = CharField(Users
)
    product = CharField(Products)
    quantity = IntegerField()

class Product_tags(BaseModel):
    product = CharField(Products)
    tag = CharField(Tags)

class Transactions(BaseModel):
    buyer = CharField(Users
)
    product = CharField(Products)
    purchased_items = IntegerField()
    bought_on_date = DateTimeField()
