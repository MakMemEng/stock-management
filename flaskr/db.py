import sqlite3

DATABASE = 'database.db'


def create_materials_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS materials (name, inventory, price)")
    con.close()
