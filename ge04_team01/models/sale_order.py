from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def apply_discount(self):
        for sale_order in self:
            sale_order.pricelist_id = self.env['product.pricelist'].search([('name', '=', 'New Customers')])
            self.action_update_prices()
