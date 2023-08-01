from odoo import http
from odoo.http import request


class MotorcycleRegistryController(http.Controller):

    @http.route(['/motorcycle_registry/get_mileage'], type='json', auth='public', website=True)
    def get_mileage(self):
        registries = http.request.env['motorcycle.registry'].sudo().search([])
        return {'total_mileage': sum(registries.mapped('current_mileage'))}
