# Copyright (c) 2025, Kalp Dalsania and contributors
# For license information, please see license.txt

import frappe
from frappe import _
import json

@frappe.whitelist()
def create_student(**kwargs): 
    data = kwargs.get('data')
    if isinstance(data, str):
        data = json.loads(data)
    
    student = frappe.get_doc({
        "doctype": "Student",
        "stu_id": data.get("stu_id"),
        "stu_name": data.get("stu_name"),
        "stu_dob": data.get("stu_dob"),
        "stu_doe": data.get("stu_doe"),
        "stu_gender": data.get("stu_gender"),
        "stu_percentage": float(data.get("stu_percentage")),
        "stu_notes": data.get("stu_notes"),
        "stu_academics": [
            {
                "doctype": "Subjects",
                "parentfield": "stu_academics",
                "sub_name": acad.get("sub_name"),
                "sub_marks": float(acad.get("sub_marks")),
                "sub_total": float(acad.get("sub_total"))
            } for acad in data.get("stu_academics", [])
        ]
    })
    student.insert()
    frappe.db.commit()
    
    return {"message": _(f"Student {student.stu_name} created successfully."), "student_id": student.name}
