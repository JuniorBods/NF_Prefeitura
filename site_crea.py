import ofxparse
import sqlite3

# Open OFX file and parse data
ofx_file = open("Bradesco_02052022_102734.OFX", "rb")
ofx = ofxparse.OfxParser.parse(ofx_file)

# Connect to SQLite database
conn = sqlite3.connect("bank_data.db")
cursor = conn.cursor()

# Create table if it does not exist
table_create_query = """
CREATE TABLE IF NOT EXISTS bank_transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id TEXT,
    type TEXT,
    date TEXT,
    amount FLOAT,
    name TEXT,
    memo TEXT
);
"""
cursor.execute(table_create_query)

# Insert transactions into database
for account in ofx.accounts:
    for transaction in account.statement.transactions:
        insert_query = """
        INSERT INTO bank_transactions (
            account_id,
            type,
            date,
            amount,
            name,
            memo
        ) VALUES (?,?,?,?,?,?);
        """
        cursor.execute(
            insert_query,
            (
                account.account_id,
                transaction.type,
                str(transaction.date),
                float(transaction.amount),
                transaction.payee,
                transaction.memo,
            ),
        )

# Commit changes and close database connection
conn.commit()
conn.close()