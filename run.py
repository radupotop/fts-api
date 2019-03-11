from pathlib import Path

from model import Products, SearchProducts, db


db.connect()


def do_query(terms: str):
    query = (
        Products.select(Products, SearchProducts.rank())
        .join(SearchProducts, on=(Products.id == SearchProducts.rowid))
        .where(SearchProducts.match(terms))
        .order_by(SearchProducts.rank())
        .limit(10)
    )
    return query


query = do_query('fat face shirt check')


for row in query:
    print(row.rank, row.product, row.brand)
