import sqlite3

conn = sqlite3.connect('/Users/zengzewei/Documents/Go/my_db.db')

cur = conn.cursor()


def insert(path):
    cur.execute("INSERT INTO bqb (path) VALUES (?)", (path,))
    conn.commit()
    conn.close()

def findAll():
    for row in cur.execute("SELECT * FROM bqb"):
        print row


if __name__ == '__main__':
    # insert("test")
    findAll()