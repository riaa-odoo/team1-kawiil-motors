import re

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry'
    _rec_name = 'registry_number'
    _sql_constraints = [
        ('vin_unique', 'UNIQUE(vin)', 'Odoopsie! Another registration for this VIN Number already exists.')
    ]

    
    registry_number = fields.Char('Registry Number', copy=False, required=True, readonly=True, default='New')
    vin = fields.Char(string='VIN', required=True)
    # first_name = fields.Char(string='First Name', required=True)
    # last_name = fields.Char(string='Last Name', required=True)
    picture = fields.Image(string='Photograph')
    current_mileage = fields.Float(string='Current Mileage')
    license_plate = fields.Char(string='License Plate Number')
    certificate_title = fields.Binary(string='Certificate of Title')
    registry_date = fields.Date(string='Registration Date')

    # Owner fields
    owner_id = fields.Many2one(comodel_name='res.partner', ondelete='restrict')
    owner_phone = fields.Char(related='owner_id.phone')
    owner_email = fields.Char(related='owner_id.email')
    
    # Vehicles fields
    make = fields.Char(compute='_compute_from_vin')
    model = fields.Char(compute='_compute_from_vin')

    # This method works, but it's better to filter the recordset before iterating over it, like in the example below                
    # @api.constrains('license_plate')
    # def _check_license_plate_size(self):
    #     pattern = '^[A-Z]{1,3}\d{1,4}[A-Z]{0,2}$'
    #     for registry in self
    #         if registry.license_plate:
    #             match = re.match(pattern, registry.license_plate)
    #             if not match:
    #                 raise ValidationError('Odoopsie! Invalid License Plate')
    
    # This is a better solution than the code above.
    
    @api.constrains('license_plate')
    def _check_license_plate_size(self):
        pattern = '^[A-Z]{1,3}\d{1,4}[A-Z]{0,2}$'
        for registry in self.filtered(lambda r: r.license_plate):
            match = re.match(pattern, registry.license_plate)
            if not match:
                raise ValidationError('Odoopsie! Invalid License Plate')
 
    @api.constrains('vin')
    def _check_vin_pattern(self):
        pattern = '^[A-Z]{4}\d{2}[A-Z0-9]{2}\d{5}$'
        for registry in self.filtered(lambda r: r.vin):
            match = re.match(pattern, registry.vin)
            if not match:
                raise ValidationError('Odoopsie! Invalid VIN')
            if not registry.vin[0:2] == 'KA':
                raise ValidationError('Odoopsie! Only motorcycles from Kauil Motors are allowed')
                
                    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('New')) == ('New'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(vals_list)
    
    @api.depends('vin')
    def _compute_from_vin(self):
        registries_with_vin = self.filtered(lambda r: r.vin)
        registries_with_vin._check_vin_pattern()
        for registry in registries_with_vin:
            registry.make = registry.vin[:2]
            registry.model = registry.vin[2:4]
        for registry in (self - registries_with_vin):
            registry.make = False
            registry.model = False