# Copyright (c) 2025, admin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class frmcall(Document):
	@frappe.whitelist()
	def frm_call(self,msg):
		return "Hello This message from frm_Call"
