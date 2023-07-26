# Inherit the motorcycle.registry model and add the portal.mixin
from odoo import fields, models


class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _inherit = ["motorcycle.registry", "portal.mixin"]

    is_public = fields.Boolean("Public", default=False)

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
