import frappe

def get_context(context):
    context.doc = frappe.get_all('Demo Doctype', fields=['first_name', 'last_name'])

    item = frappe.get_doc("Demo Doctype", "trushti-Siddhapura")  # Fetch the specific document
    context.child_table_data = item.childtable  # Access child table data