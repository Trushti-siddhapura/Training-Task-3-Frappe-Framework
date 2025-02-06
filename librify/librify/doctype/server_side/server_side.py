# Copyright (c) 2025, admin and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class serverside(Document):
	
	
	def validate(self):
		pass
@frappe.whitelist()
def insert_record():
	data = frappe.new_doc("view doctype")
	data.label="Manan"
	data.age=12
	data.hobby="Gaming"

	data.insert()

	frappe.db.commit()
	return "Record inserted successfully"
