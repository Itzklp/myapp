frappe.ready(function() {
    frappe.web_form.validate = () => {
        frappe.msgprint("name enterd")
        console.log("Inside validate")
    }
    frappe.web_form.on("prod_name", () => {
        frappe.msgprint("name enterd")
        console.log("inside event")
    });
    frappe.web_form.after_load = () => {
        console.log("Inside After Load")
        frappe.msgprint("Inside After Load")
    }
})