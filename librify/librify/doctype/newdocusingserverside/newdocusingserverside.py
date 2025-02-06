# # Copyright (c) 2025, admin and contributors
# # For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class newdocusingserverside(Document):



	# def validate(self):
	# 	self.save_document()


	# def save_document(self):
	# 	doc = frappe.new_doc("client side Scripting")
	# 	doc.label="Mitali",
	# 	doc.age=12
	# 	doc.save()


	# def validate(self):
	# 	self.delete_document()


	# def delete_document(self):
	# 	doc = frappe.get_doc("client side Scripting","dvvlfici2f")
	# 	doc.delete()



# def validate(self):
# 	self.get_list()


# def get_list():
# 	doc=frappe.db.get_list("client side Scripting",fields=["label","age"])
# 	frappe.msgprint(_("the name is {0} and {1}").format(label,age))

	# def validate(self):
	# 	self.get_value()

	# def get_value(self):
	# 	fname,age = frappe.db.get_value("client side Scripting","This is for server side scripting get docs file",["label","age"])
	# 	frappe.msgprint(_("The Parent First name is {0} and age is {1}").format(fname,age))
    

	# def validate(self):
	# 	self.set_value()

	# def set_value(self):
	# 	frappe.db.set_value("client side Scripting","this is for server side scripting get docs file","age",20)

	# 	fname,age=frappe.db.get_value("client side Scripting","this is for server side scripting get docs file",["label","age"])
	# 	frappe.msgprint(_("the message whould be {0} and {1}").format(fname,age))
    

	def validate(self):
		self.for_sql()

	def for_sql(self):
		data = frappe.db.sql("""
					select * from `tabclient side Scripting`""")
		for d in data:
			frappe.msgprint(_("the print message is basically {0} and {1}").format(data.label,data.age))
