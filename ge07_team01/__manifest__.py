{
    "name": "GE07 Team 01",
    "summary": "Seventh group task.",
    "description": """
Automates the creation of a motorcycle registry when the delivery is validated. Adds a 'Sale Order' buttton to the
registry's form view, to trace the sale order of it. Also adds a Lot ID field to the registry's list view and a
Registry ID to the stock.lot's list view.
Developers: [DIZR] Diego Zúñiga Rodríguez, [RIAA] Ricardo Alonso, [JIVP] Jordan Vega, [COAL] Corinne Angélica
Task ID: GE7
Task URL: https://www.odoo.com/web#id=3427405&cids=17&menu_id=4720&action=4665&active_id=3427418&model=project.task&view_type=form
    """,
    "version": "1.0.0",
    "category": "Custom Developoment",
    "license": "OPL-1",
    "depends": ["ge06_team01", "motorcycle_registry", "sale", "stock"],
    "data": [
        "views/stock_lot_inherit.xml",
        'views/motorcycle_registry_inherit.xml'
    ],
    "author": "Odoo Inc",
    "website": "www.odoo.com",
    "application": True
}
