// Copyright (c) 2025, Kalp Dalsania and contributors
// For license information, please see license.txt

frappe.ui.form.on("Student", {
	
});

frappe.ui.form.on("Subjects", {
    sub_marks: function(frm, cdt, cdn) {
        checkMarks(frm,cdt,cdn);
    },
    sub_total: function(frm,cdt,cdn) {
        checkMarks(frm,cdt,cdn);
    }
});

function checkMarks(frm,cdt,cdn){
    let row = locals[cdt][cdn];  

        if (row.sub_marks < 0) {
            frappe.msgprint(__('Obtained Marks cannot be negative'));
            frappe.model.set_value(cdt, cdn, 'sub_marks', 0.0);
        }

        if (row.sub_total < 0) {
            frappe.msgprint(__('Total Marks cannot be negative'));
            frappe.model.set_value(cdt, cdn, 'sub_marks', 0.0);
        }

        if(row.sub_total < row.sub_marks){
            frappe.msgprint(__('Total Marks cannot be less than Obtained Marks'));
            frappe.model.set_value(cdt, cdn, 'sub_marks', 0.0);
            frappe.model.set_value(cdt, cdn, 'sub_total', 0.0);
        }
}