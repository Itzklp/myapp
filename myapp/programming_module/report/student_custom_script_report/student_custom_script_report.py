# Copyright (c) 2025, Kalp Dalsania and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {"label": "Student ID", "fieldname": "stu_id", "fieldtype": "Data", "width": 120},
        {"label": "Student Name", "fieldname": "stu_name", "fieldtype": "Data", "width": 150},
        {"label": "DOB", "fieldname": "stu_dob", "fieldtype": "Date", "width": 150},
        {"label": "DOE", "fieldname": "stu_doe", "fieldtype": "Date", "width": 150},
        {"label": "Gender", "fieldname": "stu_gender", "fieldtype": "Data", "width": 150},
        {"label": "Percentage", "fieldname": "stu_percentage", "fieldtype": "Float", "width": 100},
        {"label": "Grade", "fieldname": "stu_grade", "fieldtype": "Select", "width": 100, "options": "A+\nA\nB+\nB\nC\nD\nE\nF"},
        {"label": "Notes", "fieldname": "stu_notes", "fieldtype": "Data", "width": 200},
        {"label": "Subject Name", "fieldname": "sub_name", "fieldtype": "Data", "width": 150},
        {"label": "Marks", "fieldname": "sub_marks", "fieldtype": "Int", "width": 80},
        {"label": "Total Marks", "fieldname": "sub_total", "fieldtype": "Int", "width": 100},
        {"label": "Indent", "fieldname": "indent", "fieldtype": "Int", "width": 80}
    ]

def get_data(filters=None):
    conditions = {}
    if filters:
        if filters.get("stu_id"):
            conditions["stu_id"] = filters["stu_id"]
        if filters.get("stu_name"):
            conditions["stu_name"] = ["like", f"%{filters['stu_name']}%"]
        if filters.get("stu_gender"):
            conditions["stu_gender"] = filters["stu_gender"]
        if filters.get("stu_grade"):
            conditions["stu_grade"] = filters["stu_grade"]
        if filters.get("stu_percentage"):
            conditions["stu_percentage"] = [">=", float(filters["stu_percentage"])]

    student_list = frappe.get_all("Student", fields=["name", "stu_id", "stu_name", "stu_dob", "stu_doe", "stu_gender", "stu_percentage", "stu_grade", "stu_notes"], filters=conditions)
    data = []

    for student in student_list:
        data.append({
            "stu_id": student["stu_id"],
            "stu_name": student["stu_name"],
            "stu_dob": student["stu_dob"],
            "stu_doe": student["stu_doe"],
            "stu_gender": student["stu_gender"],
            "stu_percentage": student["stu_percentage"],
            "stu_grade": student["stu_grade"],
            "stu_notes": student["stu_notes"],
            "sub_name": None,
            "sub_marks": None,
            "sub_total": None,
            "indent": 0
        })

        student_subjects = frappe.get_all(
            "Subjects", 
            filters={"parent": student["name"]}, 
            fields=["sub_name", "sub_marks", "sub_total"]
        )

        total_marks_obtained = 0
        total_max_marks = 0

        for subject in student_subjects:
            data.append({
                "stu_id": None,
                "stu_name": None, 
                "stu_dob": None,
                "stu_doe": None,
                "stu_gender": None,
                "stu_percentage": None,
                "stu_notes": None,
                "sub_name": subject["sub_name"],  
                "sub_marks": subject["sub_marks"],
                "sub_total": subject["sub_total"],
                "indent": 1  
            })

            total_marks_obtained += subject["sub_marks"]
            total_max_marks += subject["sub_total"]

        data.append({
            "stu_id": None,
            "stu_name": None,
            "stu_dob": None,
            "stu_doe": None,
            "stu_gender": None,
            "stu_percentage": None,
            "stu_notes": None,
            "sub_name": "Total",
            "sub_marks": total_marks_obtained,
            "sub_total": total_max_marks,
            "indent": 1 
        })

    return data