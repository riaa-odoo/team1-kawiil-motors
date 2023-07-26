{
    "name": "Generate serial number as a VIN",
    "summary": "Compute serial number from a VIN",
    "description": """
    This module create a serial number using the same format as a VIN, 
    the format is only available for products wich 'detailed_type' = 'motorcycle'
        Developer: [DIZR] Diego Zúñiga Rodríguez
        Task ID: GE6
        Task URL: https://www.odoo.com/web#id=3426312&cids=17&menu_id=4720&action=4043&model=project.task&view_type=form
    """,
    "version": "0.1",
    "category": "Kauil/Training",
    "license": "OPL-1",
    "depends": ["stock"],
    "data": [
        'data/serial_number_data.xml',
    ],
    "author": "Odoo Inc",
    "website": "www.odoo.com",
    "application": True, 
}
