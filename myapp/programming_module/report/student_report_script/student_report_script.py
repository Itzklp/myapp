# Copyright (c) 2025, Kalp Dalsania and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	columns = getColumns()
	filteredData = getData(filters)

	if not filteredData:
		frappe.msgprint("No Data Found!")
		return columns,filteredData
	
	data = []

	for i in filteredData:
		row = frappe._dict({
			"stu_id":i.stu_id,
			"stu_name":i.stu_name,
			"stu_gender":i.stu_gender,
			"stu_percentage":i.stu_percentage,
			"stu_grade":i.stu_grade,
			"stu_status":i.stu_status
		})
		data.append(row)

	charts = getChart(data)
	reportSummary = getReportSummary(data)

	return columns, data, None, charts, reportSummary


def getData(filters=None):
	conditions = getConditions(filters)
	data = frappe.get_all(
		doctype="Student",
		fields=['stu_id','stu_name','stu_gender','stu_percentage','stu_grade','stu_status'],
		filters = conditions
	)

	return data

def getConditions(filters=None):
	conditions = {}
	for key, values in filters.items():
		if filters.get(key):
			conditions[key] = values
	return conditions

def getChart(data):

	if not data:
		return None
	
	labels = ['Percentage >= 75','Percentage < 75']

	dataSets = []

	percentData = {
		'Percentage >= 75':0,
		'Percentage < 75':0
	}

	for i in data:
		if float(i.stu_percentage) >= 75.00:
			percentData['Percentage >= 75'] += 1
		else:
			percentData['Percentage < 75'] += 1
	dataSets.append({
		'name':'Percentage Status',
		'values':[percentData.get('Percentage >= 75'),percentData.get('Percentage < 75')]
	})

	chart = {
		'data':{
			'labels':labels,
			'datasets':dataSets
		},
		'type':'pie',
		'height':300
	}

	return chart

def getReportSummary(data):

	if not data:
		return None

	marksAbove75, marksBelow75 = 0, 0

	for i in data:
		if float(i.stu_percentage) >= 75.00:
			marksAbove75 += 1
		else:
			marksBelow75 += 1

	return  [
		{		
			'value':marksAbove75,
			'indicator':'Green',
			'label':'Marks Above 75',
			'datatype':'Float'
		},
		{
			'value':marksBelow75,
			'indicator':'Red',
			'label':'Marks Above 75',
			'datatype':'Float'
		}
	]

def getColumns():
	return [
		{
			"fieldname":"stu_id",
			"label": ("Student Id"),
			"fieldtype":"Data",
			"width":"120"
		},
		{
			"fieldname":"stu_name",
			"label": ("Student Name"),
			"fieldtype":"Data",
			"width":"120"
		},
		{
			"fieldname":"stu_gender",
			"label": ("Gender"),
			"fieldtype":"Link",
			"width":"120",
			"options":"Gender"
		},
		{
			"fieldname":"stu_percentage",
			"label": ("Percentage"),
			"fieldtype":"Read Only",
			"width":"120"
		},
		{
			"fieldname":"stu_status",
			"label": ("Status"),
			"fieldtype":"Read Only",
			"width":"120",
		},
		{
			"fieldname":"stu_grade",
			"label": ("Grade"),
			"fieldtype":"Read Only",
			"width":"120",
		}
	]