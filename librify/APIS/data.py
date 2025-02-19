import frappe

@frappe.whitelist(allow_guest=True)
def get_person(fname):
    doc = frappe.get_all("Person", filters={"fname": fname}, fields=["fname","sname","age"])
    return doc

    # doc1 = frappe.new_doc("Person")
    # doc1.insert()
    # frappe.db.commit()
    # return doc1
# @frappe.whitelist()
# def get_person():
#     return "API is working!"
