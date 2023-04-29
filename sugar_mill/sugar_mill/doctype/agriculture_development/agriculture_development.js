// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Agriculture Development', {
	update(frm) {
	    debugger
        frm.clear_table("agriculture_development_item")
		frm.refresh_field("agriculture_development_item")
	    var basel = "",preeathing ="",earth="",rainy="";
		
		var checkedB = frm.get_field('basel').get_value();
        if (checkedB) 
        {
           	basel = "Basel";
        }
        else 
        {
            basel = "False";
        }
        
        var checkedP = frm.get_field('pre_earthing').get_value();
        if (checkedP) 
        {
           	preeathing = "Pre-Earth";
        }
        else 
        {
            preeathing = "False";
        }
        
        var checkedE = frm.get_field('earth').get_value();
        if (checkedE) 
        {
           	earth = "Earthing";
        }
        else 
        {
            earth = "False";
        }
        
        var checkedR = frm.get_field('rainy').get_value();
        if (checkedR) 
        {
           	rainy = "Rainy";
        }
        else 
        {
            rainy = "False";
        }
       	frm.call	({
			method:"Calculate_Fertilizer",
			doc:frm.doc,
			args:{
				doctype:"Agriculture Development",
				basel:basel,
				preeathing:preeathing,
				earth:earth,
				rainy:rainy,
                croptype : frm.doc.crop_type,
                cropvariety : frm.doc.crop_variety,
				area:parseFloat(frm.doc.area),
				},
			callback: function(r) {
					frappe.msgprint("Loaded")
					frm.refresh_field('table_9');
			}
		})
	
	}
});




