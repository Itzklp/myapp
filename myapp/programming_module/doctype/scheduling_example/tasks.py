import string
import frappe
import random

def all():
    pass

def cron():
    letters = string.ascii_letters
    note =  "".join(random.choice(letters) for i in range(10))

    newNote = frappe.get_doc({
        "doctype":"Scheduling Example",
        "title":note
    })
    newNote.insert()
    frappe.db.commit()

