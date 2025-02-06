// Copyright (c) 2025, admin and contributors
// For license information, please see license.txt

frappe.ui.form.on("client for button", {
	refresh(frm){
            frm.add_custom_button(__("Button One"),function(){
                frappe.call({
                    method:"librify.librify.doctype.server_side.server_side.insert_record",
                    callback:function(response){
                        if(response.message){
                            frappe.msgprint(response.message)
                        }
                    },
                });
                
            });
	},
});
