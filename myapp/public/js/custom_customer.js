frappe.ui.form.on("Customer", {
    refresh(frm) {
        console.log("Inside Customer")
        frm.page.remove_inner_button('Get Customer Group Details', 'Actions')
    },
    onload(frm) {
        console.log("Inside Customer")
        frm.page.remove_inner_button('Get Customer Group Details', 'Actions')
    }
});
