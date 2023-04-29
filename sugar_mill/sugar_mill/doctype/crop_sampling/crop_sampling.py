# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CropSampling(Document):
	def on_trash(self):
		doc = frappe.db.get_list("Cane Master")  #fields=["plantation_status", "name","form_number"
		for a in doc:
			eachdoc= frappe.get_doc("Cane Master",a.name)
			if self.id == eachdoc.name:
				eachdoc.plantation_status="New"
				eachdoc.save()
				break

