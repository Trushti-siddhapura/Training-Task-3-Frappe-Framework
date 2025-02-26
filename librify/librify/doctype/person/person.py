import frappe
import json
from frappe.model.document import Document


class Person(Document):
    pass
 	

@frappe.whitelist(allow_guest=True)
def Add_person(doc):
    doc=json.loads(doc)
    new_person = frappe.get_doc({
        "doctype":"Person",
        "fname":doc["fname"],
        "sname":doc["sname"],
        "age":doc["age"]
    })
    new_person.insert()
    frappe.db.commit()
    return {"message":"Person Added Successfully"}
    
