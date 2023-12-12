contacts = []

def add_contact():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    contacts.append({"Name": name, "Phone": phone_number})
    print(f'Contact "{name}" added to the contact book.')

def view_contact_list():
    if not contacts:
        print("Contact book is empty.")
    else:
        print("Contact List:")
        for contact in contacts:
            print(f"Name: {contact['Name']}\tPhone: {contact['Phone']}")

def search_contact():
    keyword = input("Enter name or phone number to search: ")
    results = [contact for contact in contacts if keyword.lower() in contact['Name'].lower() or keyword in contact['Phone']]
    if not results:
        print(f"No contacts found with '{keyword}'.")
    else:
        print("Search Results:")
        for contact in results:
            print(f"Name: {contact['Name']}\tPhone: {contact['Phone']}")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['Name'].lower() == name.lower():
            contact['Phone'] = input("Enter new phone number: ")
            print(f'Contact "{name}" updated.')
            return
    print(f'Contact "{name}" not found in the contact book.')

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['Name'].lower() == name.lower():
            contacts.remove(contact)
            print(f'Contact "{name}" deleted.')
            return
    print(f'Contact "{name}" not found in the contact book.')

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact_list()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting the contact book program. Thank You for useing Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4/5/6).")