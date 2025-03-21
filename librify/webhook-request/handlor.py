import frappe

@frappe.whitelist(allow_guest=True)
def process_webhook():
    print("error10")
    data = {
            "fname": frappe.request.form.get("fname"),
            "sname": frappe.request.form.get("sname"),
            "age": frappe.request.form.get("age"),
        }
    print("Extracted Data:", data)

    worker_doc = frappe.get_doc({
            "doctype":"worker",
            "fname":data["fname"],
            "sname":data["sname"],
            "age":data["age"]
        })
    worker_doc.insert()
    frappe.db.commit()
    return {"success": True, "data": data}
    

    # except Exception as e:
    #     print("Error:", str(e))
    #     return {"error": str(e)}
