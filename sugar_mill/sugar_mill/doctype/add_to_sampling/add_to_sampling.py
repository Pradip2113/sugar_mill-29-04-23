# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

# from datetime import datetime


class AddToSampling(Document):
    @frappe.whitelist()
    def list(self):
        #  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        village_items = [d.village_link for d in self.village]
        condition_1 = "{}".format("  or  ".join(["d.area == '{}'".format(name) for name in village_items]))
        circle_office_items = [d.circle_office_link for d in self.circle_office]
        condition_2 = "{}".format("  or  ".join(["d.circle_office == '{}'".format(name) for name in circle_office_items]))
        crop_variety_items = [d.crop_variety_link for d in self.crop_variety]
        condition_3 = "{}".format("  or  ".join(["d.crop_variety == '{}'".format(name) for name in crop_variety_items]))
        crop_type_items = [d.crop_type_link for d in self.crop_type]
        condition_4 = "{}".format("  or  ".join(["d.crop_type == '{}'".format(name) for name in crop_type_items]))
        if condition_1 == "":
            frappe.throw("Please fill up village")
        if condition_2 == "":
            frappe.throw("Please fill up circle_office")
        if condition_3 == "":
            frappe.throw("Please fill up crop_variety")
        if condition_4 == "":
            frappe.throw("Please fill up crop_type")

        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        doc = frappe.db.get_list(
            "Cane Master",
            fields=[
                "grower_name",
                "form_number",
                "name",
                "plantattion_ratooning_date",
                "area",
                "circle_office",
                "crop_variety",
                "plantation_status",
                "season",
                "crop_type",
            ],
        )
        for d in doc:
            # frappe.msgprint(str(d.plantattion_ratooning_date))
            if (
                d.plantation_status == "New"
                and (
                    str(self.from_date)
                    <= str(d.plantattion_ratooning_date)
                    <= str(self.to_date)
                )
                and (self.season == d.season)
                and eval(condition_1)
                and eval(condition_2)
                and eval(condition_3)
                and eval(condition_4)
            ):
                # if(self.village == d.area) and (self.circle_office == d.circle_office) and (self.crop_variety == d.crop_variety):
                self.append(
                    "cane_master_data",
                    {
                        "id": d.name,
                        "grower_name": d.grower_name,
                        "form_number": d.form_number,
                        "plantattion_ratooning_date": d.plantattion_ratooning_date,
                        "plantation_status": d.plantation_status,
                        "area": d.area,
                        "circle_office": d.circle_office,
                        "crop_variety": d.crop_variety,
                        "season": d.season,
                    },
                )
        if not self.get("cane_master_data"):
            frappe.throw("The record You are looking for are not available")


    @frappe.whitelist()
    def selectall(self):
        children = self.get("cane_master_data")
        if not children:
            return
        all_selected = all([child.check for child in children])
        value = 0 if all_selected else 1
        for child in children:
            child.check = value

    def before_save(self):
        for row in self.get("cane_master_data"):
            if row.check:
                doc = frappe.new_doc("Crop Sampling")
                doc.id = row.id
                doc.grower_name = row.grower_name
                doc.form_number = row.form_number
                doc.plantattion_ratooning_date = row.plantattion_ratooning_date
                doc.plantation_status = "To Sampling"
                doc.area = row.area
                doc.circle_office = row.circle_office
                doc.crop_variety = row.crop_variety
                doc.season = row.season
                doc.insert()

        poc = frappe.db.get_list("Cane Master")  # fields=["plantation_status", "name","form_number"
        for i in self.get("cane_master_data"):
            if i.check:
                for a in poc:
                    eachdoc = frappe.get_doc("Cane Master", a.name)
                    if i.id == eachdoc.name:
                        eachdoc.plantation_status = "To Sampling"
                        eachdoc.save()
                        break

    def on_trash(self):
        doc = frappe.db.get_list("Cane Master")  # fields=["plantation_status", "name","form_number"
        for i in self.get("cane_master_data"):
            if i.check:
                for a in doc:
                    eachdoc = frappe.get_doc("Cane Master", a.name)
                    if i.id == eachdoc.name:
                        eachdoc.plantation_status = "New"
                        eachdoc.save()
                        break

        moc = frappe.db.get_list("Crop Sampling", fields=["id", "name"])  # fields=["plantation_status", "name","form_number"
        for j in self.get("cane_master_data"):
            if i.check:
                for c in moc:
                    if j.id == c.id:
                        frappe.delete_doc("Crop Sampling", c.name)
                        break
