import os
import pickle

# Text File Operations
def read_contacts_text(file_name):
    try:
        with open(file_name, 'r') as file:
            contacts = file.readlines()
        return [contact.strip() for contact in contacts]
    except FileNotFoundError:
        print(f"{file_name} not found. No contacts to display.")
        return []
    except Exception as e:
        print(f"Error reading {file_name}: {e}")
        return []

def write_contact_text(file_name, contact):
    try:
        with open(file_name, 'a') as file:
            file.write(contact + '\n')
    except Exception as e:
        print(f"Error writing to {file_name}: {e}")

def remove_contact_text(file_name, contact):
    try:
        contacts = read_contacts_text(file_name)
        if contact in contacts:
            contacts.remove(contact)
            with open(file_name, 'w') as file:
                for c in contacts:
                    file.write(c + '\n')
            print(f"Contact {contact} removed successfully.")
        else:
            print(f"Contact {contact} not found.")
    except Exception as e:
        print(f"Error removing contact from {file_name}: {e}")

# Binary File Operations
def save_contacts_binary(file_name, contacts):
    try:
        with open(file_name, 'wb') as file:
            pickle.dump(contacts, file)
    except Exception as e:
        print(f"Error saving to {file_name}: {e}")

def load_contacts_binary(file_name):
    try:
        with open(file_name, 'rb') as file:
            contacts = pickle.load(file)
        return contacts
    except FileNotFoundError:
        print(f"{file_name} not found. No contacts to load.")
        return []
    except Exception as e:
        print(f"Error loading {file_name}: {e}")
        return []

# User Interaction
def add_contact(file_name_text, file_name_binary, name, phone):
    contact = f"{name}: {phone}"
    write_contact_text(file_name_text, contact)
    
    contacts = load_contacts_binary(file_name_binary)
    contacts.append(contact)
    save_contacts_binary(file_name_binary, contacts)

def remove_contact(file_name_text, file_name_binary, name):
    contacts = load_contacts_binary(file_name_binary)
    contact_to_remove = next((c for c in contacts if c.startswith(name)), None)
    
    if contact_to_remove:
        remove_contact_text(file_name_text, contact_to_remove)
        
        contacts.remove(contact_to_remove)
        save_contacts_binary(file_name_binary, contacts)
    else:
        print(f"Contact {name} not found in the list.")

def display_contacts(file_name_text):
    contacts = read_contacts_text(file_name_text)
    if contacts:
        print("\nContacts List:")
        for contact in contacts:
            print(contact)
    else:
        print("No contacts available.")

# Main Function
def main():
    file_name_text = "contacts.txt"
    file_name_binary = "contacts.dat"

    while True:
        print("\nContact Management System")
        print("1. Display Contacts")
        print("2. Add Contact")
        print("3. Remove Contact")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_contacts(file_name_text)
        elif choice == '2':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(file_name_text, file_name_binary, name, phone)
        elif choice == '3':
            name = input("Enter name to remove: ")
            remove_contact(file_name_text, file_name_binary, name)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Plea
