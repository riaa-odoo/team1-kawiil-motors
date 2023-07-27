# Inherit the motorcycle.registry model and add the portal.mixin
from odoo import models


class MotorcycleRegistry(models.Model):
    _inherit = "motorcycle.registry"
