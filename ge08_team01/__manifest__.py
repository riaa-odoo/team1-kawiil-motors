{
    "name": "GE08 Team 01",
    "summary": "Eighth group task.",
    "description": """
Handle portal views (tree and form), allows to a costumer edit its registries and make it public or private.
Search for public registries based on: owner's name, country or state; motorcycle's make or model.
Search function to computed fields implemented.
Developers: [RIAA] Ricardo Alonso, [DIZR] Diego Zúñiga
Task ID: GE8
Task URL: https://www.odoo.com/web#id=3427407&cids=17&menu_id=4720&action=4665&active_id=3427418&model=project.task&view_type=form
    """,
    "version": "0.1",
    "category": "Custom Developoment",
    "license": "OPL-1",
    "data": [
        "views/motorcycle_registry_portal_templates.xml",
        "views/motorcycle_registry_inherit.xml"
    ],
    "depends": ["ge07_team01", "motorcycle_registry", "sale"],
    "author": "Odoo Inc",
    "website": "www.odoo.com",
    "application": True
}
