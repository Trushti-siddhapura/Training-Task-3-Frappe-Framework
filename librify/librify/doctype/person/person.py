import frappe
from frappe.model.document import Document


class Person(Document):
    pass
 	

@frappe.whitelist()
def Add_person(fname,sname,age):
    doc = frappe.get_doc({
        "doctype":"Person",
        "fname":fname,
        "sname":sname,
        "age":age
    })
    Person.insert()
    frappe.db.commit()
    return {"message":"Person Added Successfully"}

