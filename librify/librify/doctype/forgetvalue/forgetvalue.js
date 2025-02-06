// Copyright (c) 2025, admin and contributors
// For license information, please see license.txt

frappe.ui.form.on("forgetvalue", {





    after_save:function(frm){
        frappe.msgprint(__("The full name is '{0}'",
            [frm.doc.fname+ " "+frm.doc.mname+" "+frm.doc.lname ]))
    }
});
