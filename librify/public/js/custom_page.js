frappe.pages["custom_page"].on_page_load = function(wrapper){
    let page = frappe.ui.make_app_page({
        parent :wrapper,
        title : "Custom Page",
        single_column:true
    });
    let dialog = new frappe.ui.Dialog({
        title:"Add new Person",
        fields:[
            {
                label:"First_name",
                fieldname:"fname",
                fieldtype:"Data",
            },
            {
                label:"Second_name",
                fieldname:"sname",
                fieldtype:"Data",
            },
            {
                label:"Age",
                fieldname:"age",
                fieldtype:"Int",
            }
            
        ],
        primary_action_label:"Submit",
        primary_action(values){
            frappe.call({
                method:"librify.librify.doctype.person.person.Add_person",
                args:{
                       doc:{
                        doctype:"Person",
                        fname:values.fname,
                        sname:values.sname,
                        age:values.age
                    }
                },
                callback:function(response){
                    if(response.message){
                        frappe.msgprint("Person added successfully!");
                        dialog.hide();
                    }
                    else{
                        frappe.msgprint("failed to add person")
                    }
                } 
            });
        }
    });
    dialog.show();
}