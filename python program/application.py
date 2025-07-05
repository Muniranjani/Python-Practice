# DB CONNECTION
import sqlite3

# ADDRESS BOOK APPLICATION
# AUTHOR: VENKATESAN BE, CSE

class AddressBook:
    def giveContactDetails(self):
        contactName = input("Enter person name: ").strip()
        emailid = input("Enter email id: ").strip()
        address = input("Enter address: ").strip()
        return {"name": contactName, "email": emailid, "address": address}

def main():
    # Connect to the SQLite database
    connection = sqlite3.connect("academy.db")
    cursor = connection.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contactdetails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            address TEXT NOT NULL
        )
    ''')
    connection.commit()  # Ensure the table creation is saved

    choice = 'y'

    while choice.lower() == 'y':
        print("\n1. Add New Contact\n2. Display Contacts\n3. Total Contacts Count")
        try:
            response = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if response == 1:
            contact1 = AddressBook()  # Object creation
            contact = contact1.giveContactDetails()  # Method calling

            try:
                # Insert the new contact into the database
                cursor.execute('''
                    INSERT INTO contactdetails (name, email, address)
                    VALUES (?, ?, ?)
                ''', (contact['name'], contact['email'], contact['address']))
                connection.commit()  # Save the changes to the database
                print("Contact successfully added.")
            except sqlite3.IntegrityError as e:
                print(f"Failed to add contact: {e}")

        elif response == 2:
            cursor.execute("SELECT name, email, address FROM contactdetails")
            result = cursor.fetchall()
            if result:
                print("\nContact List:")
                for row in result:
                    print(f"Name: {row[0]}, Email: {row[1]}, Address: {row[2]}")
            else:
                print("No contacts found.")

        elif response == 3:
            cursor.execute("SELECT COUNT(*) FROM contactdetails")
            result = cursor.fetchone()
            print(f"\nTotal Contacts: {result[0]}")

        else:
            print("Invalid choice. Please select a valid option.")

        choice = input("\nPress 'y' to continue, or any other key to exit: ")

    # Close the database connection
    connection.close()
    print("Database connection closed.")

if __name__ == "__main__":
    main()
