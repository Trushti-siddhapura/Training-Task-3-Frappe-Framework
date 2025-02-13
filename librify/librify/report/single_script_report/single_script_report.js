// Copyright (c) 2025, admin and contributors
// For license information, please see license.txt

frappe.query_reports["single Script Report"] = {
	"filters": [
			{
				"fieldname":"fname",
				"label":__("First_name"),
				"fieldtype":"Link",
				"options":"Person"
			},
			{
				"fieldname":"sname",
				"label":__("Second_name"),
				"fieldtype":"Data",
				
			},
			{
				"fieldname":"age",
				"label":__("Age"),
				"fieldtype":"Int",
			}
	]	
};
