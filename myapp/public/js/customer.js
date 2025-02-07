frappe.ui.form.on("Customer", {
    refresh(frm) {
        console.log("Inside Customer refresh 4535");
        setTimeout(() => {
            // $('.btn[aria-expanded="false"][data-bs-toggle="dropdown"]').each(function() {
            //     if ($(this).text().trim() === "Actions") {
            //         $(this).hide();
            //     }
            // });
            frm.page.remove_inner_button('Get Customer Group Details', 'Actions')
        }, 500);
    }
});
