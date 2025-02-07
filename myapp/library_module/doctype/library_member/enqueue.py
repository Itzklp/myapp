import frappe
from frappe import enqueue

@frappe.whitelist()
def generate_large_report():
    enqueue(process_large_report, queue='long', timeout=1500,at_front=True)

def process_large_report():
    report_data = []
    for i in range(100000):
        report_data.append({'data': i})
    frappe.log("Large report generated successfully.")
