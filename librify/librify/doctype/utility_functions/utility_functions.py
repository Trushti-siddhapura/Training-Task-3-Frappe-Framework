# Copyright (c) 2025, admin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate,format_date,now,getdate,add_to_date,pretty_date,comma_and


class UtilityFunctions(Document):
	pass

@frappe.whitelist()
def get_formatted_date():
	today=nowdate()
	nowtime = now()
	Get_Date=getdate()
	formatted  = format_date(today,"dd-MM-yyyy")
	add10days = add_to_date(today,months=6)
	isotime = pretty_date(now())
	commanend=comma_and([1,2,3])
	cache = frappe.cache()
	return {
		"date":today,
		"formated_date":formatted,
		"Nowtime":nowtime,
		"Get_Date":Get_Date,
		"add_10_days" : add10days,
		"iso_time":isotime,
		"commanend" :commanend,
		"cache":cache
	}