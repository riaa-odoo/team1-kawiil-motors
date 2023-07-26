from odoo import models, fields


class MotorcycleRegistry(models.Model):
    _inherits = {"stock.lot": "lot_id"}

    lot_id = fields.Many2one("stock.lot", string="Lot ID")
