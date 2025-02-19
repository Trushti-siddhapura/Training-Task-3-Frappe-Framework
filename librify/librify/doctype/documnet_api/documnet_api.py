# Python file (documnet_api.py)
import frappe
from frappe.model.document import Document

class DocumnetAPI(Document):  # Match the DocType name spelling
    pass

@frappe.whitelist()
def get_name():
        doc = frappe.get_doc("Person", "PR-00006")
        frappe.db.commit()
        doc2 = doc.delete("Person")
        return {'fname':doc.fname},doc2
