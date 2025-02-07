import frappe

def after_insert_customer(doc, method):
    if doc.customer_group:
        frappe.msgprint(f"Customer Group: {doc.customer_group}")
        update_customer_group_count(doc)
    else:
        frappe.msgprint("No Customer Group selected.") 

def update_customer_group_count(doc):
    frappe.msgprint(f"Filtering by Customer Group: {doc.customer_group}")
    count = frappe.db.count("Customer", filters={"customer_group": doc.customer_group})
    frappe.msgprint(f"Customer Group Count: {count}")
    doc.custom_customer_group_count = count