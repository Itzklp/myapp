# Copyright (c) 2025, Kalp Dalsania and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Images(Document):
	pass

@frappe.whitelist()
def call_fun(msg):
	return f'Hello {msg} Pal!'
    # frappe.msgprint(f"Hello {msg}")