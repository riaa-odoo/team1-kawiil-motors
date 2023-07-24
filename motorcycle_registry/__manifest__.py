{
    "name": "Motorcycle Registry",
    
    "summary": "Manage Registration of Motorcycles",
    
    "description": """
    Motorcycle Registry
====================
This Module is used to keep track of the Motorcycle Reistration and Ownership of each motorcycled of the brand.
    """,
    
    "version": "0.1",
    
    "category": "Kauil/Registry",
    
    "license": "OPL-1",
    
    "depends": ["stock", "website"],
    
    "data": [
        "security/motorcycle_registry_groups.xml",
        "security/ir.model.access.csv",
        'data/registry_data.xml',
        "views/motorcycle_registry_menuitems.xml",
        "views/motorcycle_registry_views.xml",
        "views/product_template_inherit.xml",
        "views/motorcycle_registry_templates.xml",
    ],
    
    "demo": [
        "demo/motorcycle_registry_demo.xml",
        "demo/product_demo.xml",
    ],
    
    "author": "kauil-motors",
    
    "website": "www.odoo.com",
    
    "application": True,
    
}