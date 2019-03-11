import csv
from model import db, Products


def build_db():
    db.connect()
    db.create_tables((Products,))


def import_db():
    with open('./search_dataset.csv') as f:
        reader = csv.reader(f)
        with db.atomic():
            for row in reader:
                Products.create(orig_id=row[0], product=row[1], brand=row[2])


if __name__ == '__main__':
    build_db()
    import_db()
