import frappe

def get_persons():
    return frappe.db.get_list("Person", fields=["fname", "sname", "age"])
