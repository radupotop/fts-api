import peewee as pw

db = pw.SqliteDatabase('products.db')


class BaseModel(pw.Model):
    class Meta:
        database = db


class Products(BaseModel):
    orig_id = pw.IntegerField()
    product = pw.CharField()
    brand = pw.CharField()

class SearchProducts(BaseModel):
    '''
    Virtual table with FTS5.
    '''
    product_fk = pw.ForeignKeyField(Products, backref='search')
    product_brand = pw.CharField()
