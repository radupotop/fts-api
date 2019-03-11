from model import db, Products, SearchProducts

db.connect()

query = (
    Products.select()
    .join(SearchProducts, on=(Products.id == SearchProducts.rowid))
    .where(SearchProducts.match('fat face'))
)

