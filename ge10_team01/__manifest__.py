{
    'name': 'GE10 Team 01',
    'summary': 'Tenth group task.',
    'description': '''
This module adds a widget available through the webside editor. This widget displays the summation of all the 
'current_mileage' fields of the Motorcycle Registry module. Users may customize this widget with the next attributes:
layout; box or text, background color, border color, text color.
Developers: [RIAA] Ricardo Alonso
Task ID: 3427414
Task URL: https://www.odoo.com/web#id=3427414&cids=17&menu_id=4720&action=4665&active_id=3427418&model=project.task&view_type=form
    ''',
    'version': '1.0.0',
    'category': 'Custom Developoment',
    'license': 'OPL-1',
    'data': [
        'views/snippets/snippets.xml',
        'views/snippets/s_registry_miles.xml'
    ],
    'depends': ['motorcycle_registry'],
    'author': 'Odoo Inc',
    'website': 'www.odoo.com',
    'application': True,
    'assets': {
        'website.assets_wysiwyg': ['ge10_team01/static/src/snippets/s_registry_miles/options.js']
    }
}
