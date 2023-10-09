import sqlite3


def create_table(table_name):
    conn = sqlite3.connect("mydb.db")
    conn.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name varchar(100),
                address varchar(100),
                salary int
                );
    ''')
    conn.close()

# create_table("mytable")


def add_to_db():
    conn = sqlite3.connect("mydb.db")

    while True:

        name = input("enter company's name: ")
        address = input("enter the address: ")
        salary = int(input("enter the salary: "))

        conn.execute(f'''INSERT INTO COMPANY(name, address, salary) 
                    VALUES (?,?,?);
        ''', (name, address, salary))
        conn.commit()
        if input("Continue (y|n)? ").lower().startswith("n"):
            break

    conn.close()


def select_from_table():
    pass
