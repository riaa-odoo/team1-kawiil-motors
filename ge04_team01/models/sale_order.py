from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    is_new_customer = fields.Boolean(related="partner_id.is_new_customer")

    def apply_discount(self):
        for sale_order in self:
            if sale_order.is_new_customer:
                sale_order.pricelist_id = self.env['product.pricelist'].search([('name', '=', 'New Customers')])
                self.action_update_prices()
