from odoo import api, fields, models


class RepairOrder(models.Model):
    _inherit = "repair.order"

    vin = fields.Char(string='VIN', required=False)
    current_mileage = fields.Float(string='Current Mileage')
    registry_id = fields.Many2one(
        "motorcycle.registry", string="Registry ID", compute="_compute_vin", store=True)

    partner_id = fields.Many2one(related="registry_id.owner_id")
    sale_order_id = fields.Many2one(related="registry_id.sale_order_id")
    lot_id = fields.Many2one(related="registry_id.lot_id")
    product_id = fields.Many2one(related="registry_id.lot_id.product_id")

    @api.depends("vin")
    def _compute_vin(self):
        for order in self:
            registry = self.env['motorcycle.registry'].search(
                [('vin', '=', order.vin)])
            order.registry_id = registry
