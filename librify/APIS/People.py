import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_people():
    persons = frappe.get_doc("Person","PR-00011")
    return persons