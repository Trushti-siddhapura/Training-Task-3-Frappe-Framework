// Copyright (c) 2025, admin and contributors
// For license information, please see license.txt

frappe.ui.form.on('client side Scripting', {
	refresh(frm) {
	
	    frm.add_custom_button(__("Click Me!!!"),function(){
	        console.log("This is my print statment!")
	        frappe.msgprint("The button was clicked")
	    })
	}
})

