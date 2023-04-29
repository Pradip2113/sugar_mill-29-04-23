# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AgricultureDevelopment(Document):
	@frappe.whitelist()
	def Calculate_Fertilizer(self,doctype,basel,preeathing,earth,rainy,area,croptype,cropvariety):
		data = frappe.db.sql("""
                      select tabitem.item_code 'ItemCode',tabitem.item_name 'ItemName',tabitem.item_group 'Itemgroup',tabitem.name  , ceiling(ifnull(tabdose.quantity,0)* %(area)s) 'Baselqty',
					ceiling(ifnull(tabPreEarth.quantity,0) * %(area)s)  'preearthqty',ceiling(ifnull(tabEarthing.quantity,0)* %(area)s)  'earthingqty',ceiling(ifnull(tabRainy.quantity,0) * %(area)s)  'Rainyqty'
					from `tabItem` tabitem 
					left join
					(
						select tabDosetypeItem.fertilize_name,tabDosetypeItem.parent,tabDosetypeItem.quantity,tabDosetypeItem.uom
						from `tabDose Type` tabDosetype
						inner join `tabDose Type Item` tabDosetypeItem
						on tabDosetypeItem.parent =  tabDosetype.name  where dose = %(basel)s and  tabDosetype.crop_type = %(croptype)s  and tabDosetype.cane_variety = %(cropvariety)s
					) tabdose on tabdose.fertilize_name = tabitem.item_code
					left join
					(
						select tabDosetypeItem.fertilize_name,tabDosetypeItem.parent,tabDosetypeItem.quantity,tabDosetypeItem.uom
						from `tabDose Type` tabDosetype
						inner join `tabDose Type Item` tabDosetypeItem
						on tabDosetypeItem.parent =  tabDosetype.name  where dose = %(preearth)s and  tabDosetype.crop_type = %(croptype)s  and tabDosetype.cane_variety = %(cropvariety)s
					) tabPreEarth on tabPreEarth.fertilize_name = tabitem.item_code
					left join
						(
						select tabDosetypeItem.fertilize_name,tabDosetypeItem.parent,tabDosetypeItem.quantity,tabDosetypeItem.uom
					from `tabDose Type` tabDosetype
					inner join `tabDose Type Item` tabDosetypeItem
					on tabDosetypeItem.parent =  tabDosetype.name  where dose = %(earthing)s and  tabDosetype.crop_type = %(croptype)s  and tabDosetype.cane_variety = %(cropvariety)s
						) tabEarthing on tabEarthing.fertilize_name = tabitem.item_code
					left join
						(
						select tabDosetypeItem.fertilize_name,tabDosetypeItem.parent,tabDosetypeItem.quantity,tabDosetypeItem.uom
					from `tabDose Type` tabDosetype
					inner join `tabDose Type Item` tabDosetypeItem
					on tabDosetypeItem.parent =  tabDosetype.name  where dose = %(rainy)s and  tabDosetype.crop_type = %(croptype)s  and tabDosetype.cane_variety = %(cropvariety)s
						) tabRainy on tabRainy.fertilize_name = tabitem.item_code
					where tabitem.item_group = 'Fertilize' order by  tabitem.item_code
										""",{
							'basel': basel	,	'preearth': preeathing,'earthing': earth, 'rainy': rainy,'area' : area , 'croptype' : croptype, 'cropvariety' : cropvariety
						},  as_dict=1)	
		if data:
			# frappe.msgprint(str(data))
			for row in data:			
				self.append("agriculture_development_item",{
								"item":row.ItemCode,
								"basel":row.Baselqty,
								"pre_earthing":row.preearthqty,
								"earth":row.earthingqty,
								"rainy":row.Rainyqty,
								"total": float(row.Baselqty) + float(row.preearthqty) + float(row.earthingqty) +  float(row.Rainyqty)
								
								}
								)	
		else :
			return 0
		return data
  
		# if(basel == "True"):
		# 	databasel = frappe.ge_all("Dose Type",filters={'dose': 'Basel'},fields=["*"])
		# 	frappe.msgprint(str(databasel))
		# 	for d in databasel:				
		# 		frappe.msgprint(d.area)

		# if(preeathing == "True"):
		# 	datapreeathing = frappe.get_all("Dose Type",filters={'dose': 'Pre-Earth'},fields=["*"])
		# 	frappe.msgprint(str(datapreeathing))
		# 	for d in datapreeathing:				
		# 		frappe.msgprint(d.area)
    
		# if(earth == "True"):
		# 	dataearth = frappe.get_all("Dose Type",filters={'dose': 'Earthing'},fields=["*"])
		# 	frappe.msgprint(str(dataearth))
		# 	for d in dataearth:				
		# 		frappe.msgprint(d.area)

		# if(rainy == "True"):
		# 	datarainy = frappe.get_all("Dose Type",filters={'dose': 'Rainy'},fields=["*"])
		# 	frappe.msgprint(str(datarainy))
		# 	for d in datarainy:				
		# 		frappe.msgprint(d.area)



