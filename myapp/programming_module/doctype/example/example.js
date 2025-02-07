// Copyright (c) 2025, Kalp Dalsania and contributors
// For license information, please see license.txt

frappe.ui.form.on("Example", {

    enable:function(frm){
        // frm.call({
        //     doc:frm.doc,
        //     method:'call',
        //     args:{
        //         msg:'Kalp'
        //     },
        //     freeze:true,
        //     freeze_message:(__("This is freeze methode.")),
        //     callback:function(r){
        //     }
        // });
        frappe.call({
            method:'myapp.programming_module.doctype.images.images.call_fun',
            args:{
                msg:'Kalp'
            },
            freeze:true,
            freeze_message:(__("This is freeze Messsage.")),
            callback:function(r){
                frappe.msgprint(r.message)
            }
        });
    }
    // refresh: function(frm){
    //     frm.set_intro("Welcome to this doctype!!!");
    // },
	// after_save: function(frm){
    //     let name = frm.doc.name1;
    //     let float = frm.doc.float;

    //     frappe.msgprint(__('The Value is :- ' + name));
    // },

    // before_submit: function(frm){
    //     frappe.msgprint(__("The Form is submitted successfuly!!!!!!"));
    //     if (frm.doc.float > 50.000){
    //         frm.set_df_property('float','hidden',1);
    //     }
    // } 
});
