from tkinter import *
from tkinter import messagebox

contacts=[]

root=Tk()
root.title("Contact Book")
root.geometry("500x375")


#defining functions
def addContact():
    win=Toplevel(root)
    win.title("Add Contact")
    win.geometry("300x200")

    Label(win,text="Name").grid(row=0,column=0)
    Label(win,text="Phone").grid(row=1,column=0)
    Label(win,text="Email").grid(row=2,column=0)
    Label(win,text="Address").grid(row=3,column=0)

    name = Entry(win)
    phone = Entry(win)
    email = Entry(win)
    address = Entry(win)

    name.grid(row=0, column=1)
    phone.grid(row=1, column=1)
    email.grid(row=2, column=1)
    address.grid(row=3, column=1)

    def saveContact():
        contact={
            "name":name.get(),
            "phone":phone.get(),
            "email":email.get(),
            "address":address.get()
        }

        contacts.append(contact)
        messagebox.showinfo("Success","Contact Added")
        win.destroy()

    Button(win, text="Save", command=saveContact).grid(row=4, column=1)


def updateContact():
    win = Toplevel(root)
    win.title("Update Contact")
    win.geometry("300x200")

    Label(win, text="Enter Name").grid(row=0, column=0)
    name_search = Entry(win)
    name_search.grid(row=0, column=1)

    Label(win, text="New Phone").grid(row=1, column=0)
    new_phone = Entry(win)
    new_phone.grid(row=1, column=1)

    Label(win, text="New Email").grid(row=2, column=0)
    new_email = Entry(win)
    new_email.grid(row=2, column=1)

    Label(win, text="New Address").grid(row=3, column=0)
    new_address = Entry(win)
    new_address.grid(row=3, column=1)

    def update_contact():
        for contact in contacts:
            if contact["name"] == name_search.get():
                contact["phone"] = new_phone.get()
                contact["email"] = new_email.get()
                contact["address"] = new_address.get()
                messagebox.showinfo("Success", "Contact Updated")
                win.destroy()
                return

        messagebox.showerror("Error", "Contact Not Found")

    Button(win, text="Update", command=update_contact).grid(row=4, column=1,pady=20)


def viewContact():
    win = Toplevel(root)
    win.title("View Contacts")
    win.geometry("350x200")

    listbox = Listbox(win, width=50)
    listbox.pack(pady=10)

    if not contacts:
        listbox.insert(END,"No Contacts Available")
    else:
        for contact in contacts:
            listbox.insert(END, contact["name"] + " | " + contact["phone"] + " | " + contact["email"])


def searchContact():
    win = Toplevel(root)
    win.title("Search Contact")
    win.geometry("300x300")

    Label(win, text="Enter Name or Phone").pack()

    search = Entry(win)
    search.pack(pady=5)

    result = Listbox(win, width=40)
    result.pack(pady=10)

    def search_now():
        query = search.get()
        result.delete(0, END)

        found=False

        for contact in contacts:
            if contact["name"] == query or contact["phone"] == query:
                result.insert(END, contact["name"] + " | " + contact["phone"] + " | " + contact["email"])
                found=True

        if not found:
            result.insert(END, "Contact Not Found")

    Button(win, text="Search", command=search_now).pack()


def deleteContact():
    win = Toplevel(root)
    win.title("Delete Contact")
    win.geometry("250x150")

    Label(win, text="Enter Name").pack()

    name = Entry(win)
    name.pack(pady=5)

    def delete_now():
        for contact in contacts:
            if contact["name"] == name.get():
                contacts.remove(contact)
                messagebox.showinfo("Deleted", "Contact Deleted")
                win.destroy()
                return

        messagebox.showerror("Error", "Contact Not Found")

    Button(win, text="Delete", command=delete_now).pack(pady=5)


#defining buttons

Label(root, text="CONTACT BOOK", font=("Arial", 20)).pack(pady=20)

Button(root,text="Add Contact",width=20,command=addContact).pack(pady=5)
Button(root,text="Update Contact",width=20,command=updateContact).pack(pady=5)
Button(root,text="Search Contact",width=20,command=searchContact).pack(pady=5)
Button(root,text="View Contacts",width=20,command=viewContact).pack(pady=5)
Button(root,text="Delete Contact",width=20,command=deleteContact).pack(pady=5)


root.mainloop()
