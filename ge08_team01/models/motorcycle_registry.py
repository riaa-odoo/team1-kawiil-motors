# Inherit the motorcycle.registry model and add the portal.mixin
from odoo import fields, models


class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _inherit = ["motorcycle.registry", "portal.mixin"]

    is_public = fields.Boolean("Public", default=False)

    model = fields.Char(search = '_search_model')
    make = fields.Char(search = '_search_make')

    def _get_portal_return_action(self):
        self.ensure_one()
        return self.env.ref("motorcycle_registry.registry_list_action")

    # portal.mixin override
    def _compute_access_url(self):
        super()._compute_access_url()
        for registry in self:
            registry.access_url = f"/my/registries/{registry.id}"

    def _set_is_public(self):
        self.ensure_one()
        self.is_public = not self.is_public

    def _search_model(self, operator, value):
        domain = []
        if len(value) == 1:
            domain = ['|', ('vin', operator, f'__{value}_%'), ('vin', operator, f'___{value}%')]
        elif len(value) == 2:
            domain = [('vin', operator, f'__{value}%')]
            
        print(domain)
        return domain

    def _search_make(self, operator, value):
        domain = []
        if len(value) == 1:
            domain = ['|', ('vin', operator, f'_{value}%'), ('vin', operator, f'{value}_%')]
        elif len(value) == 2:
            domain = [('vin', operator, f'{value}%')]
            
        print(domain)
        return domain
    