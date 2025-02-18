// Copyright (c) 2025, admin and contributors
// For license information, please see license.txt

frappe.ui.form.on("Utility Functions", {
	refresh:function(frm) {
        frappe.call({
            method:"librify.librify.doctype.utility_functions.utility_functions.get_formatted_date",
            callback:function(response){
                if(response.message){
                    frappe.msgprint("Today's Date:"+ response.message.formated_date)
                    frappe.msgprint(response.message.Nowtime)
                    frappe.msgprint(response.message.Get_Date)
                    frappe.msgprint(response.message.add_10_days)
                    frappe.msgprint(response.message.iso_time)
                    frappe.msgprint(response.message.commanend)
                    frappe.msgprint(response.message.cache)

                }
            }
        })

	},
});
    

