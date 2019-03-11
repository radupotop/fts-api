from pathlib import Path

from model import Products, SearchProducts, db


db.connect()

def parse_file():
    _file = Path('./input.txt').read_text()
    rows = _file.split('\n')
    return tuple(do_query(r) for r in rows)


def do_query(terms: str):
    query = (
        Products.select(Products, SearchProducts.rank())
        .join(SearchProducts, on=(Products.id == SearchProducts.rowid))
        .where(SearchProducts.match(terms))
        .order_by(SearchProducts.rank())
        .limit(10)
    )
    return query

if __name__ == '__main__':
    results = parse_file()

    for r in results:
        for row in r:
            print('{}, {}, {}'.format(row.rank, row.product, row.brand))
