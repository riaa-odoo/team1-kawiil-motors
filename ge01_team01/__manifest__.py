{
    "name": "Motorcycle Registry",
    "summary": "Manage Registration of Motorcycles",
    "description": """
    Motorcycle Registry
====================
    Developer: [DIZR] Diego Zúñiga Rodríguez
    Task ID: GE1
    Task URL: https://www.odoo.com/web#id=3426296&cids=17&menu_id=4720&action=4043&model=project.task&view_type=form
This Module is used to add a filter for products based on 'detailet_type' field, also set it as default in the Sales/Products/Products.
    """,
    "version": "0.1",
    "category": "Kauil/Training",
    "license": "OPL-1",
    "depends": ["stock", "sale"],
    "data": [
        "views/product_template_inherit.xml",
        "views/product_views_inherit.xml",
    ],
    "author": "Odoo Inc",
    "website": "www.odoo.com",
    "application": True,
}
