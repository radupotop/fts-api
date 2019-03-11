import csv
from model import db, Products, SearchProducts


def build_db():
    db.connect()
    db.create_tables((Products, SearchProducts))


def import_db():
    with open('./search_dataset.csv') as f:
        reader = csv.reader(f)
        with db.atomic():
            for row in reader:
                Products.create(orig_id=row[0], product=row[1], brand=row[2])


def create_virt_table():
    '''
    Create virtual table with FTS5 search.
    '''
    db.connect()
    db.execute_sql(
        'INSERT INTO searchproducts SELECT product || " " || brand FROM products'
    )


if __name__ == '__main__':
    build_db()
    import_db()
    create_virt_table()
