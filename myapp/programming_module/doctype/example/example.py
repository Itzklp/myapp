# Copyright (c) 2025, Kalp Dalsania and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import time

class Example(Document):
    pass
    # @frappe.whitelist()
    # def call(self,msg):
    #     time.sleep(5)
    #     frappe.msgprint(msg)

    # def after_save(self):
    #     frappe.frappe.msgprint('Message')

    # def validate(self):
    #     frappe.frappe.msgprint('From Example')    
    # def validate(self):
    #     frappe.msgprint('Inside validate')

    # def on_save(self):
    #     frappe.msgprint('Inside on_save')

    # def before_insert(self):
    #     frappe.msgprint('From Examplet')

    # def after_insert(self):
    #     frappe.msgprint('Inside after_insert')

    # def before_submit(self):
    #     frappe.msgprint('Inside before_submit')

    # def on_submit(self): 
    #     frappe.msgprint('Inside on_submit')

    def on_cancel(self):  
        frappe.msgprint('Inside on_cancel')