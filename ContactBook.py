import tkinter as tk
from tkinter import messagebox, simpledialog

class Contact:
    def _init_(self, store_name, phone_number, email, address):
        self.store_name = store_name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def _str_(self):
        return f"{self.store_name}, {self.phone_number}, {self.email}, {self.address}"


class ContactManager:
    def _init_(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(contact)

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term in contact.store_name or search_term in contact.phone_number]
        return results

    def update_contact(self, phone_number, new_details):
        for contact in self.contacts:
            if contact.phone_number == phone_number:
                contact.store_name = new_details.get("store_name", contact.store_name)
                contact.phone_number = new_details.get("phone_number", contact.phone_number)
                contact.email = new_details.get("email", contact.email)
                contact.address = new_details.get("address", contact.address)
                return True
        return False

    def delete_contact(self, phone_number):
        self.contacts = [contact for contact in self.contacts if contact.phone_number != phone_number]


def main():
    manager = ContactManager()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            store_name = input("Enter store name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(store_name, phone_number, email, address)
            manager.add_contact(contact)
        
        elif choice == '2':
            manager.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            results = manager.search_contact(search_term)
            if results:
                for result in results:
                    print(result)
            else:
                print("No contacts found.")

        elif choice == '4':
            phone_number = input("Enter the phone number of the contact to update: ")
            store_name = input("Enter new store name (leave blank to keep current): ")
            new_phone_number = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            new_details = {
                "store_name": store_name if store_name else None,
                "phone_number": new_phone_number if new_phone_number else None,
                "email": email if email else None,
                "address": address if address else None,
            }
            updated = manager.update_contact(phone_number, new_details)
            if updated:
                print("Contact updated.")
            else:
                print("Contact not found.")

        elif choice == '5':
            phone_number = input("Enter the phone number of the contact to delete: ")
            manager.delete_contact(phone_number)
            print("Contact deleted.")

        elif choice == '6':
            break

        else:
            print("Invalid choice, please try again.")
main()


class ContactManagerGUI:
    def _init_(self, root):
        self.manager = ContactManager()
        self.root = root
        self.root.title("Contact Management System")

        self.label = tk.Label(root, text="Contact Management System")
        self.label.pack()

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack()

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack()

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.pack()

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()

    def add_contact(self):
        store_name = simpledialog.askstring("Input", "Enter store name:")
        phone_number = simpledialog.askstring("Input", "Enter phone number:")
        email = simpledialog.askstring("Input", "Enter email:")
        address = simpledialog.askstring("Input", "Enter address:")
        if store_name and phone_number and email and address:
            contact = Contact(store_name, phone_number, email, address)
            self.manager.add_contact(contact)
            messagebox.showinfo("Info", "Contact added successfully")

    def view_contacts(self):
        contacts = "\n".join(str(contact) for contact in self.manager.contacts)
        messagebox.showinfo("Contact List", contacts if contacts else "No contacts available.")

    def search_contact(self):
        search_term = simpledialog.askstring("Input", "Enter name or phone number to search:")
        results = self.manager.search_contact(search_term)
        if results:
            messagebox.showinfo("Search Results", "\n".join(str(result) for result in results))
        else:
            messagebox.showinfo("Search Results", "No contacts found.")

    def update_contact(self):
        phone_number = simpledialog.askstring("Input", "Enter the phone number of the contact to update:")
        store_name = simpledialog.askstring("Input", "Enter new store name (leave blank to keep current):")
        new_phone_number = simpledialog.askstring("Input", "Enter new phone number (leave blank to keep current):")
        email = simpledialog.askstring("Input", "Enter new email (leave blank to keep current):")
        address = simpledialog.askstring("Input", "Enter new address (leave blank to keep current):")
        new_details = {
            "store_name": store_name if store_name else None,
            "phone_number": new_phone_number if new_phone_number else None,
            "email": email if email else None,
            "address": address if address else None,
        }
        updated = self.manager.update_contact(phone_number, new_details)
        if updated:
            messagebox.showinfo("Info", "Contact updated successfully")
        else:
            messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self):
        phone_number = simpledialog.askstring("Input", "Enter the phone number of the contact to delete:")
        self.manager.delete_contact(phone_number)
        messagebox.showinfo("Info", "Contact deleted successfully")

root = tk.Tk()
app = ContactManagerGUI(root)
root.mainloop()