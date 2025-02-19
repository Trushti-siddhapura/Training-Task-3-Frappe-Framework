import frappe


@frappe.whitelist()
def  get_data(fname):
    doc = frappe.db.get_list("Person",filters={"fname":fname,"date":[">","1-01-2025"]},fields=["count(fname) as count","gender"],group_by="gender")  
    doc2 = frappe.db.set_value("Person","PR-00001","age",90) 
    frappe.db.commit()
    return doc,doc2 