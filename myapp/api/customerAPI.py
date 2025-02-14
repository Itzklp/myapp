# Copyright (c) 2025, Kalp Dalsania and contributors
# For license information, please see license.txt

import frappe
from frappe import _
import json

@frappe.whitelist()
def fetch_customers(**kwargs):
    try:
        frappe.logger().info(f"Received kwargs: {kwargs}")
        data = kwargs.get('data')
        if isinstance(data, str):
            data = json.loads(data)
        
        # The field named custom_custom_customer_group_id is not of type int otherwise we could have filer for group_id range
        filters = data.get("filters", {})
        customers = frappe.get_all(
            "Customer",
            filters=filters,
            fields=["name", "customer_name", "customer_group", "custom_custom_customer_group_id", "email_id", "mobile_no"],
            order_by="custom_custom_customer_group_id ASC"
        )
        
        return {"message": _("Customers fetched successfully"), "customers": customers}

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Fetch Customers API Error")
        return {"error": str(e)}
