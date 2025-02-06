# Copyright (c) 2025, admin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class serversidescripting(Document):


	def validate(self):	
		frappe.msgprint("Hello This is Server Side scripting")	
	def before_save(self):
		frappe.msgprint("this is my error page")