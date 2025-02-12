// Copyright (c) 2025, admin and contributors
// For license information, please see license.txt

frappe.ui.form.on("Forsetvalue", {



	refresh:function(frm) {
        frm.set_value("fullname",frm.doc.fname+" "+frm.doc.mname+" "+frm.doc.lname)
	}
});
    