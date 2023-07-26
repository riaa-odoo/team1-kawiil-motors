from odoo import api, fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    is_new_customer = fields.Boolean("Is New Customer", compute="_compute_is_new_customer")

    @api.depends("sale_order_ids")
    def _compute_is_new_customer(self):
        domain = [("product_id.detailed_type", "=", "motorcycle")]
        old_customers = self.env["sale.order.line"].search(domain).mapped(
            "order_id").filtered(lambda s: s.state in ["sale", "done"]).mapped("partner_id")
        self.is_new_customer = True
        old_customers.is_new_customer = False
