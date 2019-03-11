All commands are run within `venv`. I use Python 3.7.x.

The `products.db` sqlite3 db file is included for convenience.
It might not run on all machines.

## Building and Usage

To build the initial product db:

    python build.py

To run:

    python run.py

The file containg the FTS queries is `input.txt`

## Structure

The models are held in `model.py`.

There is a main `Products` model and a FTS virtual table `SearchProducts`.

The virtual table has a single column (not counting the implicit `rowid`),
called `product_brand` containing the concatenated product and brand names.

These tables are created in `build.py`.
The Products table is build from the CSV file, while the SearchProducts is populated from the Products table.

`run.py` handles executing the FTS query, and uses Okapi BM25 for ranking.

There is a `sample_output.txt` file provided for convenience.

## Author

Radu Potop <radu@wooptoo.com>
