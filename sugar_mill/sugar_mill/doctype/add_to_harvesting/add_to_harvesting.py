# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AddtoHarvesting(Document):
    
    # pass
    @frappe.whitelist()
    def list(self):
        village_items = [d.village_link for d in self.village]
        condition_1 = "{}".format("  or  ".join(["d.area == '{}'".format(name) for name in village_items]))
        frappe.msgprint(str(condition_1))
    #     # frappe.msgprint("this is working")
    #     doc = frappe.db.get_list(
    #         "Crop Sampling",
    #         fields=[
    #             "name",
    #             "id",
    #             "grower_name",
    #             "form_number",
    #             "plantattion_ratooning_date",
    #             "area",
    #             "circle_office",
    #             "crop_variety",
    #             "plantation_status",
    #             "season",
    #             "brix",
    #             "no_of_pairs",
    #         ],
    #     )
    #     # frappe.msgprint(str(doc))
    #     for d in doc:
    #         # frappe.msgprint(str(d.plantattion_ratooning_date))
    #         if (d.plantation_status == "Added To Sampling"
    #             and (
    #                 str(self.from_date)
    #                 <= str(d.plantattion_ratooning_date)
    #                 <= str(self.to_date)
    #             )
    #             and (float(self.from_brix) <= float(d.brix) <= float(self.to_brix))
    #             and (
    #                 float(self.from_pairs)
    #                 <= float(d.no_of_pairs)
    #                 <= float(self.to_pairs)
    #             )
    #             and (self.season == d.season)
    #             and (self.village == d.area)
    #             and (self.circle_office == d.circle_office)
    #             and (self.crop_variety == d.crop_variety)
                
    #         ):  # d.plantation_status != "Added To Sampling" and
    #             # if(self.village == d.area) and (self.circle_office == d.circle_office) and (self.crop_variety == d.crop_variety):
    #             self.append(
    #                 "crop_sampling_data",
    #                 {
    #                     "id": d.id,
    #                     "brix": d.brix,
    #                     "no_of_pairs": d.no_of_pairs,
    #                     "grower_name": d.grower_name,
    #                     "form_number": d.form_number,
    #                     "plantattion_ratooning_date": d.plantattion_ratooning_date,
    #                     "plantation_status": d.plantation_status,
    #                     "area": d.area,
    #                     "circle_office": d.circle_office,
    #                     "crop_variety": d.crop_variety,
    #                     "season": d.season,
    #                 },
    #             )
    #     if not self.village:
    #         frappe.msgprint("Please fill up Village")
    #     if not self.circle_office:
    #         frappe.msgprint("Please fill up Circle Office")
    #     if not self.crop_variety:
    #         frappe.msgprint("Please fill up Crop Variety")
    #     if not self.season:
    #         frappe.msgprint("Please fill up Season")

    # @frappe.whitelist()
    # def selectall(self):
    #     # frappe.msgprint("go gog ")
    #     children = self.get("crop_sampling_data")
    #     if not children:
    #         return
    #     all_selected = all([child.check for child in children])
    #     value = 0 if all_selected else 1
    #     for child in children:
    #         child.check = value

    # # @frappe.whitelist()
    # # def mist(self):
    # #     for row in self.get("crop_sampling_data"):
    # #         if row.check:
    # #             self.append(
    # #                 "selected_for_harvesting",
    # #                 {
    # #                     "id": row.id,
    # #                     "brix": row.brix,
    # #                     "no_of_pairs": row.no_of_pairs,
    # #                     "grower_name": row.grower_name,
    # #                     "form_number": row.form_number,
    # #                     "plantattion_ratooning_date": row.plantattion_ratooning_date,
    # #                     "plantation_status": row.plantation_status,
    # #                     "area": row.area,
    # #                     "circle_office": row.circle_office,
    # #                     "crop_variety": row.crop_variety,
    # #                     "season": row.season,
    # #                 },
    # #             )


    # def before_save(self):
    #     for row in self.get('selected_for_harvesting'):
    #         # frappe.msgprint("agdfskjgjkg")
    #         doc=frappe.new_doc('Crop Harvesting')
    #         doc.brix =row.brix
    #         doc.no_of_pairs=row.no_of_pairs
    #         doc.id =row.id
    #         doc.grower_name=row.grower_name
    #         doc.form_number=row.form_number
    #         doc.plantattion_ratooning_date=row.plantattion_ratooning_date
    #         doc.plantation_status="Added To Harvesting"
    #         doc.area=row.area
    #         doc.circle_office=row.circle_office
    #         doc.crop_variety=row.crop_variety
    #         doc.season=row.season
    #         doc.insert()
            
    #     poc = frappe.db.get_list("Crop Sampling")
    #     for i in self.get('selected_for_harvesting'):
    #         for a in poc:
    #             eachdoc= frappe.get_doc("Crop Sampling",a.name)
    #             if i.id == eachdoc.id:
    #                 eachdoc.plantation_status="Added To Harvesting"
    #                 eachdoc.save()
    #                 break
                
    # def on_trash(self):
    #     doc =frappe.db.get_list("Crop Sampling")
    #     for i in self.get('selected_for_harvesting'):
    #         for a in doc:
    #             eachdoc= frappe.get_doc("Crop Sampling",a.name)
    #             if i.id == eachdoc.id:
    #                 eachdoc.plantation_status="Added To Sampling"
    #                 eachdoc.save()
    #                 break
                
    #     moc = frappe.db.get_list("Crop Harvesting", fields=["id","name"])
    #     for j in self.get('selected_for_harvesting'):
    #         for c in moc:
    #             if j.id == c.id:
    #                 frappe.delete_doc("Crop Harvesting",c.name)
    #                 break
