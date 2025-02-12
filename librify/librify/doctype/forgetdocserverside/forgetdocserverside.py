# Copyright (c) 2025, admin and contributors
# For license information, please see license.txt
from frappe import _
import frappe
from frappe.model.document import Document


class forgetdocserverside(Document):

	def validate(self):
		self.get_document()

	def get_document(self):
		doc = frappe.get_doc('client side Scripting',self.clientdoclink)
		frappe.msgprint(_("Thi is my value1:{0} This is my value2:{1}").format(doc.label,doc.age))



