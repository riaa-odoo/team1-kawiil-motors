{
    "name": "GE12 Team 01",
    "summary": "12th group task.",
    "description": """
Automate the portal account creation, after delivery's confirmation an email with the portal credentials is send,
only when the user does not have an account.
Developers: [DIZR] Diego Zúñiga Rodríguez
Task ID: GE12
Task URL: https://www.odoo.com/web#id=3426328&cids=17&menu_id=4720&action=4665&active_id=3426329&model=project.task&view_type=form
    """,
    "version": "1.0.0",
    "category": "Custom Developoment",
    "license": "OPL-1",
    "depends": ["ge07_team01", "motorcycle_registry"],
    "data": [
        'data/mail_template_data.xml',
    ],
    "author": "Odoo Inc",
    "website": "www.odoo.com",
    "application": True
}
