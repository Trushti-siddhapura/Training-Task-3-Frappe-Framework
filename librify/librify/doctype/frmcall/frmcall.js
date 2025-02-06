// Copyright (c) 2025, admin and contributors
// For license information, please see license.txt

frappe.ui.form.on("frmcall", {
    enable:function(frm){
        frm.call({
            doc : frm.doc,
            method : 'frm_call',
            args: {
                msg:"Hello"
            },
            callback:function(r){
                frappe.msgprint(r.message);
            }
        });
    }
});
