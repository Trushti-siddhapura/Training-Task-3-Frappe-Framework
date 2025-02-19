// JavaScript file (documnet_api.js)
frappe.ui.form.on("Documnet API", {  // Match the DocType name spelling
    refresh: function(frm) {
        frappe.call({
            method: "librify.librify.doctype.documnet_api.documnet_api.get_name",  // Match the path
            callback: function(response) {
                    frappe.msgprint("Response is: " + response.message.fname);
                    frappe.msgprint("Record Deletde successfully"+response.message)
            },
        });
    }
});