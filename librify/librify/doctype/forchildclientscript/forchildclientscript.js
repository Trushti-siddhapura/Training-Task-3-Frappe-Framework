// Copyright (c) 2025, admin and contributors
// For license information, please see license.txt

frappe.ui.form.on("forchildclientscript", {
	refresh(frm) {
	},
});

frappe.ui.form.on("forctable",{
    data:function(frm){
        frappe.msgprint("Hello This is my child table event")
    }
})
 