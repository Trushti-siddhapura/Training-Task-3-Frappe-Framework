# Copyright (c) 2025, admin and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class forgetvalueserverside(Document):
	def validate(self):
		frappe.msgprint(_("hello My full name is: '{0}'").format(self.fname + " " + self.sname + " " + self.tname))

	def after_save(self):
		frappe.msgprit(_("Hello this is my frappe page"))


	def validate(self):
		for row in self.get("childtable"):
			frappe.msgprint(_("The family member data is basically '{0}'").format(row.data))