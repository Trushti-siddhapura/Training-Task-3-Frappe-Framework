# Copyright (c) 2025, admin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class DemoDoctype(Document):
    pass  # Keep the class clean, remove the method from here

@frappe.whitelist()
def get_salary():
    return frappe.db.count("Demo Doctype", {"salary": [">", 10000]})  # Correct filter
