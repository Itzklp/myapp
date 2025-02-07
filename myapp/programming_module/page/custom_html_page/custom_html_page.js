frappe.pages['custom-html-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Custom HTML',
		single_column: true
	});

	page.set_title("My Custom HTML Page");
	page.set_indicator('Open','green')

	let $button = page.set_primary_action("Refresh",()=>{frappe.msgprint("Refresh Clicked")})
	let $button_sec = page.set_secondary_action("Quit",()=>{frappe.msgprint("Quit Called")})

	let $menu = page.add_menu_item("Delete",()=>{frappe.msgprint("Delete Clicked")})
	let $menu2 = page.add_menu_item("New",()=>{frappe.msgprint("New Clicked")})

	let field = page.add_field({
		label:'Status',
		fieldtype:'Select',
		fieldname:'Status',
		options:[
			'Open',
			'Close',
			'Cancalled'
		],
		change(){
			let x = field.get_value();
			if(x == 'Open'){
				page.set_indicator('Open','green')
			}
			else if(x == 'Close'){
				page.set_indicator('Close','yellow')
			} 
			else if(x == 'Cancalled'){
				page.set_indicator('Cancalled','red')
			}
		}

	});

	$(frappe.render_template('index',{})).appendTo(page.body);		
}