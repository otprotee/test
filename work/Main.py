import sqlite3

#intalize connection
conn = sqlite3.connect('harbour_view.db')
cursor_obj = conn.cursor()
cursor_obj.execute("DROP TABLE IF EXISTS staff")

staff_table = """
    CREATE TABLE staff (
        first_name CHAR(25) NOT NULL,
        second_name CHAR(25) NOT NULL,
        phone_number INT
    );
"""
cursor_obj.execute(staff_table)

pay_table = """
    CREATE TABLE pay(
        foreign_key INT,
        pay FLOAT, 
        hours FLOAT
    );
"""

cursor_obj.execute("INSERT INTO staff VALUES('oscar', 'thompson', '07538471316')")

s = '''SELECT * FROM staff'''
cursor_obj.execute(s)
output = cursor_obj.fetchall()
for row in output:
    print(row)
conn.commit()