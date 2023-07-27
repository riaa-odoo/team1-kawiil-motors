from odoo import models


class Picking(models.Model):
    _inherit = "stock.picking"
    
    def _action_done(self):
        res = super()._action_done()
        vals_list = []
        for line in self.move_line_ids.filtered(
                lambda l: l.product_id.detailed_type == "motorcycle" and l.state == "done"):
            vals = {
                "vin": line.lot_id.name,
                "sale_order_id": self.sale_id.id,
                "lot_ids": [line.lot_id.id]
            }
            vals_list.append(vals)
        self.env['motorcycle.registry'].create(vals_list)
        return res
