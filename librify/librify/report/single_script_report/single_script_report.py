import frappe
from frappe import _,msgprint

def execute(filters=None):
	if not filters: filters = {}

	data, columns = [], []

	columns = get_columns()
	cs_data = get_cs_data(filters)

	if not cs_data:
		msgprint(_('No records found'))
		return columns, cs_data

	data = []
	for d in cs_data:
		row = frappe._dict({
				'fname': d.fname,
				'sname': d.sname,
				'age': d.age
			})
		data.append(row)

	chart = get_chart_data(data)
	report_summary = get_report_summary(data)
	return columns, data,None ,chart,report_summary

def get_columns():
	return [
		{
			'fieldname': 'fname',
			'label': _('First_name'),
			'fieldtype': 'Data',
			'width': '120'
		},
		{
			'fieldname': 'sname',
			'label': _("Second_name"),
			'fieldtype': 'Data',
			'width': '120'
		},
		{
			'fieldname': 'age',
			'label': _('Age'),
			'fieldtype': 'Int',
			'width': '100'
		},
	
	]

def get_cs_data(filters):
	conditions = get_conditions(filters)
	if "fname" in conditions:
		conditions["name"] = conditions.pop("fname")
	data = frappe.get_all('Person',
		fields=['fname', 'sname', 'age'],
		filters=conditions,
		order_by='fname desc'
	)
	return data

def get_conditions(filters):
	conditions = {}
	for key, value in filters.items():
		if filters.get(key):
			conditions[key] = value
	return conditions

#########################chart Section#############################
def get_chart_data(data):
	if not data:
			return None
	###taking the list and there is 2 string inside it
	labels = ["Age <= 45","Age > 45"]

	##Here basically there is dictionary and inside there is key and value pair thing
	age_data={
		"Age > 45":0,
		"Age <= 45":0,
	}
	datasets = []
#############basically only count option ##########
	for entry in data:
		if entry.age<=45:
			age_data["Age <= 45"]+=1
		else:
			age_data["Age > 45"]+=1

	datasets.append({
		"name":"Age status",
		"values":[age_data.get("Age <= 45"),age_data.get("Age > 45")]
	})
	chart = {
		"data":{
			"labels":labels,
			"datasets":datasets
		},
		"type":"percentage",
		"height":300,
	}
	return chart




####################Report Summery###########################
def get_report_summary(data):
	if not data:
		return None
	
	########Simple taking teo variable####################
	age_below_45=0
	age_above_45=0

################looping for couting#######################
	for entry in data:
		if entry.age<=45:
			age_below_45+=1
		else:
			age_above_45+=1

	return [
		{
			'value': age_below_45,
			'indicator': 'Blue',
			'label': 'Age Below 45',
			'datatype': 'Int',
		},
		{
			'value': age_above_45,
			'indicator': 'red',
			'label': 'Age Above 45',
			'datatype': 'Int',
		}
	]

