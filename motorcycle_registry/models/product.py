from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    battery_capacity = fields.Selection(selection=[('xs','Small'),
                                        ('0m','Medium'),
                                        ('0l','Larga'),
                                        ('xl','Extra Large'),],
                                        copy=False
                                       )
    charge_time = fields.Float()
    curb_weight = fields.Float()
    horsepower = fields.Float()
    launch_date = fields.Date()
    make = fields.Char()
    model = fields.Char()
    range = fields.Float()
    top_speed = fields.Float()
    torque = fields.Float()
    year = fields.Integer()
    
    detailed_type = fields.Selection(selection_add=[('motorcycle','Motorcycle')], 
                            ondelete={'motorcycle': 'set product'},
                            help='A storable product is a product for which you manage stock. The Inventory app has to be installed.\n'
                            'A consumable product is a product for which stock is not managed.\n'
                            'A service is a non-material product you provide.\n'
                            'A motorcycle is a captivating symbol of freedom, power, and adventure, offering an exhilarating two-wheeled escape that combines speed, agility, and the thrill of the open road.')

    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['motorcycle'] = 'product'
        return type_mapping
    