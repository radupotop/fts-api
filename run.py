from pathlib import Path

from model import SQL, Products, SearchProducts, db

db.connect()


def parse_file():
    '''
    Parse input file with query terms.
    '''
    _file = Path('./input.txt').read_text()
    rows = _file.split('\n')
    return tuple(do_query(r) for r in rows)


def do_query(terms: str):
    '''
    Do FTS query, use Okapi BM25 ranking.
    '''
    query = (
        Products.select(Products, SearchProducts.bm25().alias('score'))
        .join(SearchProducts, on=(Products.id == SearchProducts.rowid))
        .where(SearchProducts.match(terms))
        .order_by(SQL('score').desc())
        .limit(10)
    )
    return query


def run_all():
    results = parse_file()

    for idx, r in enumerate(results):
        print(idx + 1)
        for row in r:
            print(
                '{}, {}, {}, {}'.format(row.score, row.orig_id, row.product, row.brand)
            )


if __name__ == '__main__':
    run_all()
