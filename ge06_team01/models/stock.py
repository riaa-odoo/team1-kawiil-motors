from odoo import api, models

class StockLot(models.Model):
    _inherit = 'stock.lot'
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            product = self.env['product.product'].search([("id", "=", vals['product_id'])])

            if product.detailed_type == "motorcycle":
                product_make = product.make[:2].upper()
                product_model = product.model[:2].upper()
                product_year = str(product.year)[-2:]
                vals['name'] = f"{product_make}{product_model}{product_year}{self.env['ir.sequence'].next_by_code('serial.number')}"
        return super().create(vals_list)
