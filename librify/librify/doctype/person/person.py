# Copyright (c) 2025, admin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Person(Document):
 	def get_full_name(self):
        	return f"{self.fname} {self.sname}"
	# def validate(self):
	# 	if self.age <= 18:
	# 		frappe.throw("This age is underage you can't vote!")
	# 		# frappe.msgprint("This age is underage, you can't vote!") 
#This is Comment..

# doc=frappe.get_doc("Person","This is Person 1")
# print(doc.get_full_name())
# doc=frappe.get_doc("Person","This is Person 2")
# print(doc.get_full_name())		
