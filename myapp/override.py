import frappe


def on_cancel():
    frappe.msgprint("Overridden methode")
