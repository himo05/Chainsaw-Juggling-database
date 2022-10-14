"""
A menu - you need to add the database and fill in the functions. 
"""

from database import JugglingRecordDB


database = JugglingRecordDB()

def main():
    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            display_single_record()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')


""" Get the number of catches whenver asked and make sure it is a valid int """
def get_number_catches():
    
    while True:
        try:
            catches = int(input('Enter the number of catches: '))
            return catches
        except: 
            print('Please enter a number.')


""" From the database detch all the records and return """
def get_all_records():
    records = database.get_all_records()
    return records


""" Call the getallrecords functions to get records and if the list return is not empty print all of them """
def display_all_records():
    records = get_all_records()
    if records is not None:
        if not records:
            print("No records")
        else:
            for record in records:
                print(record)
    else:
        print('Error fetching records')
    
""" When called get a certain record with the searchbyname function using the name of the player and print it if not empty or none """
def display_single_record():
    name = input('Enter player to get his/her record: ')
    record = search_by_name(name)
    if record:
        print(str(record))
    else:
        print(f'Could not find {name}\'s record')

""" Get a certain record from the database and return it """
def search_by_name(name):
    record = database.get_record(name)
    return record
    


""" Ask user for input and using that input insert the record into the database """
def add_new_record():
    name = input('Enter name of player: ')
    country = input('Enter country of player: ')
    catches = get_number_catches()

    record = search_by_name(name)

    if not record:

        return_message = database.insert_record(name, country, catches)

        if return_message:
            print('Inserted record')
        else:
            print('Error inserting record')
    
    else:
        print('Player already exist')


""" Ask user for player name and a new catch number and update the record in the database """
def edit_existing_record():


    name = input('Enter name of player to edit their record: ')
    catches = get_number_catches()
    record = search_by_name(name)

    if record:

        return_message = database.update_record(name, catches)
        if return_message:
            print('Updated record')
        else:
            print('Error updating record')
    
    else:
        print('Player does not exist')
    

""" Ask user for player name and using it delete the record from the database """
def delete_record():



    name = input('Enter name of player to delete their record: ')
    
    
    record = search_by_name(name)

    if record:

        return_message = database.delete_record(name)
        if return_message:
            print('Deleted record')
        else:
            print('Error deleting record')
    
    else:
        print('Player does not exist')
    
    


if __name__ == '__main__':
    main()