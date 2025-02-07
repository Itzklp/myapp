// Copyright (c) 2025, Kalp Dalsania and contributors
// For license information, please see license.txt

frappe.query_reports["Student Report Script"] = {
	"filters": [
		{
			"fieldname":"name",
			"label":__("Student Id"),
			"fieldtype":"Link",
			"options":"Student"
		},
		{
            "fieldname": "stu_gender",
            "label": __("Gender"),
            "fieldtype": "Link",
			"options": "Gender" 
        },
		{
			"fieldname": "stu_status",
			"label":__("Status"),
			"fieldtype":"Select",
			"options":"\nPass\nFail"
		}
	]
};
