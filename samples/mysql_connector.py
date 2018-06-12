# server_version.py - retrieve and display database server version

import MySQLdb


def insert_ec2():
    try:
        conn = MySQLdb.connect(host="localhost",
                               user="user1",
                               passwd="password",
                               db="test")
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        row = cursor.fetchone()
        print("server version:", row[0])

        query = ("INSERT INTO ec2 (aws_product_name, instanceid) VALUES (%s, %s);")
        data = ('EC2', 'i-00000000000000001')
        cursor.execute(query, data)
        conn.commit()
        emp_no = cursor.lastrowid
        print(emp_no)

    except Exception as e:
        print('Error:', e)

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    insert_ec2()
