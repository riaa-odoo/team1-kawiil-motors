from odoo import api, fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    is_new_customer = fields.Boolean("Is New Customer", compute="_compute_is_new_customer")

    @api.depends("sale_order_ids")
    def _compute_is_new_customer(self):
        # domain = [("motorcycle", "not in", "sale_order_ids.mapped('order_line').mapped('product_id.detailed_type')")]
        domain = [("product_id.detailed_type", "=", "motorcycle")]
        old_customers = self.env['sale.order.line'].search(domain).mapped('order_id').mapped('partner_id')
        self.is_new_customer = True
        for partner in old_customers:
            partner.is_new_customer = False
