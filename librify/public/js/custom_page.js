frapper.pages["custom_page"].on_page_load = function(wrapper){
    let page = frapper.ui.make_app_page({
        parent :wrapper,
        title : "Custom Page",
        single_column:true
    });
    let dialog = new frapper.ui.Dialog({
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
            frapper.call({
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
                        frapper.msgprint("Person added successfully!");
                        dialog.hide();
                    }
                    else{
                        frapper.msgprint("failed to add person")
                    }
                } 
            });
        }
    });
    dialog.show();
}