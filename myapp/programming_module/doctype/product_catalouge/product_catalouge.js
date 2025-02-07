// Copyright (c) 2025, Kalp Dalsania and contributors
// For license information, please see license.txt

frappe.ui.form.on("Product Catalouge", {
    refresh: function(frm) {
        check_stock(frm);
    },

    prod_stock: function(frm) {
        check_stock(frm);
    }
});

function check_stock(frm) {
    if (frm.doc.prod_stock === 0) {
        frappe.msgprint(__('The stock for this item is zero!'));
    }
}