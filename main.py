import requests
from config import url
import json
import sqlite3


def create_table():
    conn = sqlite3.connect('rates_db.db')
    sql_command = """CREATE TABLE if not exists rates(id integer, name text, rate real)        
    """
    conn.execute(sql_command)
    conn.close()


def drop_table(table_name):
    conn = sqlite3.connect('rates_db.db')
    sql_command = f"""DROP TABLE  {table_name}      
    """
    conn.execute(sql_command)
    conn.close()


def get_rates():
    response = requests.get(url)
    return response.json()


def archive(filename, rates, file_or_db):
    if file_or_db == "file":
        with open(f'archive/{filename}.json', 'w') as f:
            f.write(json.dumps(rates))
    elif file_or_db == "db":
        conn = sqlite3.connect('rates_db.db')
        sql_command = """INSERT INTO rates(id, name, rate) VALUES (?,?,?)
            """
        for index, rate in enumerate(rates.items()):
            conn.execute(sql_command, (index+1, rate[0], rate[1]))
        conn.commit()


create_table()
result = get_rates()
archive(result['timestamp'], result['rates'], "db")

# drop_table("rates")
