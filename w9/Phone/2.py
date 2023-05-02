import func as pm # phone_book module

def print_choice():
    print("Select instructions you need to work: ")
    print("1 - insert data from concole, (name surname phone_number format)")
    print("2 - delete data from database by name surname")
    print("3 - order data by name")
    print("4 - to insert data from csv file")
    print("5 - update data")
    print("6 - exit")

isDone = True

while isDone:
    print_choice()
    option = int(input("\n"))
    print()

    if option == 1: # Insert data (name, surname, phone_number)
        name = input("Name: ")
        surname = input("Surname: ")
        phone_number = input("Phone number: ")
        pm.connect()
        pm.insert(name, surname, phone_number)
        
    elif option == 2: # delete data by (name, surname)
        name = input("Name: ")
        surname = input("Surname: ")
        pm.delete(name, surname)

    elif option == 3: # order
        attribute = input("Attribute: ")
        pm.sort_by_attribute(attribute)

    elif option == 4: # Convert csv to pgls
        path = input("Path: ")
        pm.import_from_csv(path)

    elif option == 5: # Update
        surname = input("Enter surname: ")
        pm.change(surname)

    elif option == 6: # Exit
        pm.show()

        isDone = False
