import peewee as pw
from playhouse.sqlite_ext import FTS5Model, SearchField, SqliteExtDatabase

db = SqliteExtDatabase('products.db')


class BaseModel(pw.Model):
    class Meta:
        database = db


class Products(BaseModel):
    orig_id = pw.IntegerField()
    product = pw.CharField()
    brand = pw.CharField()


class SearchProducts(FTS5Model):
    '''
    Virtual table with FTS5.
    '''
    # The `rowid` field is created automatically
    product_brand = SearchField()

    class Meta:
        database = db
