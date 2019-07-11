import sqlite3

def make_dict(arr1, arr2):
    result = []
    if len(arr1) < 1:
        return result
    if len(arr1[0]) != len(arr2):
        raise Exception('columns and data do not match')
    for row in arr1:
        row_dict = dict()
        for j in range(len(row)):
            row_dict[arr2[j][0]] = row[j]
        result.append(row_dict)
    return result

class SQLite3Connection:
    def __init__(self, db):
        connection = sqlite3.connect(db)
        # establish the connection to the database
        self.connection = connection
    # the method to query the database
    def query_db(self, query, data=[]):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, data)
            if query.lower().find("select") >= 0:
                res = cursor.fetchall()
                columns = cursor.description
                result = make_dict(res, columns)
                print(result)
                return result
            else:
                self.connection.commit()
        except Exception as e:
            print("ERROR:", e)
            return False
    def __del__(self):
        self.connection.close()

def connectToSQLite3(db):
    return SQLite3Connection(db)
