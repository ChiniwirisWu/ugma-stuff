#install pymysql library and a database management system like mariadb that's all.
import pymysql

#table clients
myConnection = pymysql.connect(host='127.0.0.1', user='root', password='123', db='cards')
cursor = myConnection.cursor()

def select ():
    cursor.execute('SELECT * FROM client')
    counter = 1
    print('SELECT METHOD:')
    for el  in cursor.fetchall():
        print('{}) {}'.format(counter, el))
        counter += 1

def insert ():
    sql = 'INSERT INTO client (id, name, role, password, salt) VALUES (%s, %s, %s, %s, %s)'
    cursor.execute(sql, ('9483204','pepe','user','asdf','jfjeisd'))
    myConnection.commit()
    select()

def delete():
    sql = 'DELETE FROM client WHERE id = %s'
    cursor.execute(sql, ('9483204'))
    myConnection.commit()
    select()

def update():
    sql = 'UPDATE client SET name = %s WHERE name = %s'
    cursor.execute(sql, ('Buzz light year', 'julian'))
    myConnection.commit()
    select()

# insert()
# delete()
# select()
# update()
myConnection.close()
