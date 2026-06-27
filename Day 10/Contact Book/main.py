from Database import database

database.create_contacts()

while True:
    print("----------------Menu-----------------\n")
    print("1. Add contact")
    print("2. Update contact")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. View all contacts")
    print("6. Exit")
    print("\n----------------Menu-----------------")

    while True:
        try:
            choice = int(input("Choose an option : "))
            break
        except ValueError:
            print("Invalid Option")
    
    if choice == 6:
        break

    match choice:
        case 1:
            contact_id = int(input("Enter the id of the contact : "))
            name = input("Enter the name of the contact : ")
            number = input("Enter the number")
            email = input("Enter the email of the contact : ")
            database.add_contact(contact_id, name, number, email)

        case 2:
            contact_id = int(input("Enter the id of the contact you want to update : "))
            field = input("Enter the name of the field you want to update : \n'name' for Contact Name\n'phone' for Number\n'email' for Email\n")
            value = input("Enter the new value: ")
            database.update_contact(contact_id,field,value)

        case 3:
            name = input("Enter the name of the contact you want to search : ")
            database.search_contact(name)

        case 4:
            contact_id = int(input("Enter the id of the contact you want to delete : "))
            database.delete_contact(contact_id)
        case 5:
            database.view_contacts()