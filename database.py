import sqlite3

db_path = 'chainsaw_juggling_db.sqlite'


""" Create a class for the database for programs to use  """
class JugglingRecordDB():

    """ When the class is created the first thing we do is create a new table if it does not already exist """
    def __init__(self):
        with sqlite3.connect(db_path) as conn:
            conn.execute('create table if not exists records (name text, country text, catches integer)')

    """ When this function is called it will fetch all records from the database and return them in a list """
    def get_all_records(self):
        with sqlite3.connect(db_path) as conn:
            try:
                records = []
                for row in conn.execute('select * from records'):
                    records.append(row)
                return records
            except sqlite3.Error as error:
                return None

    """ When this function is called with the arguments below it will create and insert a new record into the database """
    def insert_record(self, name, country, catches):
        with sqlite3.connect(db_path) as conn:
            try:
                conn.execute('insert into records values (?, ?, ?)', (name, country, catches))
                return 'success'
            except sqlite3.Error as error:
                return None
    
    """ When this function is called with a name it will delete that record from the database using the name  """
    def delete_record(self, name):
        with sqlite3.connect(db_path) as conn:
            try:
                conn.execute('DELETE FROM records WHERE name = ?', (name,))
                return 'success'
            except sqlite3.Error as error:
                return None
    
    """ When this function is called with a name it will fetch and return that record from the database using the name  """
    def get_record(self, name):
        with sqlite3.connect(db_path) as conn:
            try:
                result = conn.execute('SELECT * FROM records WHERE name = ?', (name,))
                record = result.fetchone()
                if not record:
                    return None
                else:
                    return record
            except sqlite3.Error as error:
                return None
    
    """ When this function is called with a name and catches number it will update that record in the database using the name  """
    def update_record(self, name, catches):
        with sqlite3.connect(db_path) as conn:
            try:
                conn.execute('UPDATE records SET catches = ? WHERE name = ?', (catches, name))
                return 'success'
            except sqlite3.Error as error:
                return None

    

    

