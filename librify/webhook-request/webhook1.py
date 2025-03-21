import frappe
import json

@frappe.whitelist(allow_guest=True)
def create_record():
    # try:
        raw_data = frappe.request.data
        frappe.logger().info(f"Webhook Raw Data: {raw_data}")

        # Ensure raw_data is properly handled
        data = json.loads(raw_data or "{}")

        fname = data.get("fname")
        sname = data.get("sname")   
        age = data.get("age")

        # Validate data (avoid inserting empty records)
        # if not fname or not sname or not age:
        #     frappe.logger().error("Missing required fields")
        #     return {"status": "error", "message": "Missing required fields"}

        # Create new Worker record
        worker = frappe.get_doc({
            "doctype": "Worker",  # Ensure this matches your Doctype name
            "fname": fname,  
            "sname": sname,  
            "age": age  
        })

        worker.insert()
        frappe.db.commit()

        frappe.logger().info("Worker Created Successfully")
        return {"status": "success", "message": "Worker Created!",}

    # except Exception as e:
    #     frappe.logger().error(f"Error creating Worker: {str(e)}")
    #     return {"status": "error", "message": str(e)}