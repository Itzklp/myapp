# Copyright (c) 2025, Kalp Dalsania and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = getColumns()
    data = getData(filters)
    return columns, data

def getColumns():
     return [
        {
            "fieldname": "stu_id",
            "label": "Student ID",
            "fieldtype": "Link",
            "options": "Student",
            "width": 150
        },
        {
            "fieldname": "stu_name",
            "label": "Student Name",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "sub_name",
            "label": "Subject",
            "fieldtype": "Link",
            "options": "Subjects",
            "width": 150
        },
        {
            "fieldname": "sub_marks",
            "label": "Marks Obtained",
            "fieldtype": "Float",
            "width": 120
        },
        {
            "fieldname": "sub_total",
            "label": "Total Marks",
            "fieldtype": "Float",
            "width": 120
        },
        {
            "fieldname": "stu_percentage",
            "label": "Percentage",
            "fieldtype": "Float",
            "width": 120
        }
    ]

def getData(filters):
    conditions = getConditions(filters)
    
    academicsData = frappe.get_all(
        "Subjects",
        filters=conditions,
        fields=["parent AS stu_id", "sub_name", "sub_marks", "sub_total"]
    )
    
    studentData = frappe.get_all(
        "Student",
        filters={"name": ["in", [item['stu_id'] for item in academicsData]]},
        fields=["name AS stu_id", "stu_name"]
    )
    studentMap = {item['stu_id']: item['stu_name'] for item in studentData}
    
    resultData = []
    for record in academicsData:
        student_name = studentMap.get(record['stu_id'])
        percentage = (record['sub_marks'] / record['sub_total']) * 100 if record['sub_total'] else 0
        resultData.append({
            "stu_id": record['stu_id'],
            "stu_name": student_name,
            "sub_name": record['sub_name'],
            "sub_marks": record['sub_marks'],
            "sub_total": record['sub_total'],
            "stu_percentage": round(percentage, 2)
        })
    
    return resultData

def getConditions(filters):
    conditions = {}
    
    if filters.get("stu_id"):
        conditions["parent"] = filters.get("stu_id")
        
    if filters.get("sub_name"):
        conditions["sub_name"] = filters.get("sub_name")
    
    return conditions
