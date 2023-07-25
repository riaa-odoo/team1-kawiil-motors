{
    "name": "GE04 Team 01",
    "summary": "Fourth group task.",
    "description": """
This Module is used to add an 'Add Discount' button to the Sales Order form view, only when a new customer is detected, 
and when the order is a quotation. This button surcharges $2,500 out of the motorcycle price.
Developers: [RIAA] Ricardo Alonso, [COAL] Corinne
Task ID: 'GE4: Rebate for New Customers'
Task URL: https://www.odoo.com/web#id=3427394&cids=17&menu_id=4720&action=4665&active_id=3427418&model=project.task&view_type=form
    """,
    "version": "0.1",
    "category": "Custom Development",
    "license": "OPL-1",
    "depends": ["motorcycle_registry", "sale"],
    "data": ['data/pricelist_data.xml',
             'views/sale_order_inherit.xml'],
    "author": "Odoo Inc.",
    "website": "www.odoo.com",
    "installable": True
}
