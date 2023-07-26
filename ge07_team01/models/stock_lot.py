from odoo import models, fields


class StockLot(models.Model):
    _inherit = "stock.lot"

    registry_id = fields.Many2one("motorcycle.registry")
