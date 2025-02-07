frappe.query_reports["Subject Marks Report"] = {
    "filters": [
        {
            fieldname: "stu_id",
            label: __("Student"),
            fieldtype: "Link",
            options: "Student",
            default: null
        },
        {
            fieldname: "sub_name",
            label: __("Subject"),
            fieldtype: "Link",
            options: "Subjects",
            default: null
        }
    ]
};
