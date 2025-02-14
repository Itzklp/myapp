// Copyright (c) 2025, Kalp Dalsania and contributors
// For license information, please see license.txt

frappe.query_reports["Student Custom Script Report"] = {
	"filters": [
		{
            "fieldname": "stu_id",
            "label": __("Student ID"),
            "fieldtype": "Link",
            "reqd": 0,
			"options": "Student"
        },
        {
            "fieldname": "stu_percentage",
            "label": __("Percentage"),
            "fieldtype": "Float",
            "reqd": 0
        },
        {
            "fieldname": "stu_gender",
            "label": __("Gender"),
            "fieldtype": "Link",
            "options": "Gender",
            "reqd": 0
        },
        {
            "fieldname": "stu_grade",
            "label": __("Grade"),
            "fieldtype": "Select",
            "options": "\nA\nB\nC\nD\nF",
            "reqd": 0
        }
	],

	"onload": function(report) {
        report.page.add_inner_button(__("Sort by Grade"), function () {
            frappe.query_report.filters_by_name.stu_grade.set_value("A"); 
            frappe.query_report.refresh();
        });
    }
};
