import pymysql


host, port, user, passwd, db = 'mysql-db', 3306, 'user', 'password', 'db'


def insert(user_id, user_name):
    try:
        # Establishing a connection to DB 
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                                   cursorclass=pymysql.cursors.DictCursor)
        conn.autocommit(True)
        # Getting a cursor from Database
        cursor = conn.cursor()
        cursor.execute(f"INSERT into {db}.users (user_id, user_name, creation_date) VALUES ({user_id},'{user_name}', CURRENT_TIMESTAMP);")
        cursor.close()
        conn.close()
        result = 1 # user added
        print("inserted user",user_id ,user_name)
    except pymysql.err.IntegrityError as ie:
        result = 2 # id already exists
    except ( RuntimeError, pymysql.err.OperationalError ) as oe:
        result = 3 # Can't connect to MySQL server
    except Exception as e:
        result = 4 # unknown
    finally:
        return result
        

def select(user_id):
    try:
        # Establishing a connection to DB
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                                   cursorclass=pymysql.cursors.DictCursor)
        conn.autocommit(True)
        # Getting a cursor from Database
        cursor = conn.cursor()
        res = cursor.execute(f"SELECT * FROM {db}.users WHERE user_id = {user_id};")
        data = cursor.fetchall()
        user_name = data[0]['user_name']
        cursor.close()
        conn.close()
        result = user_name # user name
        print("selected user",user_id ,user_name)
    except IndexError as ie:
        result = 2  # no such id
    except (RuntimeError, pymysql.err.OperationalError) as oe:
        result = 3  # Can't connect to MySQL server
    except Exception as e:
        result = 4  # unknown
    finally:
        return result


def update(user_id, user_name):
    try:
        result = select(user_id)
        if(result == 2):  # no such id
            return result
        # Establishing a connection to DB
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                               cursorclass=pymysql.cursors.DictCursor)
        conn.autocommit(True)
        # Getting a cursor from Database
        cursor = conn.cursor()
        cursor.execute(f"UPDATE {db}.users SET user_name = '{user_name}' WHERE user_id = {user_id};")
        cursor.close()
        conn.close()
        result = 1  # user updated
        print("updated user",user_id, user_name)
    except IndexError as ie:
        result = 2  # no such id
    except (RuntimeError, pymysql.err.OperationalError) as oe:
        result = 3  # Can't connect to MySQL server
    except Exception as e:
        result = 4  # unknown
    finally:
        return result


def delete(user_id):
    try:
        result = select(user_id)
        if (result == 2):  # no such id
            return result
        # Establishing a connection to DB
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                                   cursorclass=pymysql.cursors.DictCursor)
        conn.autocommit(True)
        # Getting a cursor from Database
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {db}.users WHERE user_id = {user_id};")
        cursor.close()
        conn.close()
        result = 1 # user deleted
        print("deleted user",user_id)
    except IndexError as ie:
        result = 2 # no such id
    except ( RuntimeError, pymysql.err.OperationalError ) as oe:
        result = 3 # Can't connect to MySQL server
    except Exception as e:
        result = 4 # unknown
    finally:
        return result