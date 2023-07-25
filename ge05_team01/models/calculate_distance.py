from odoo import fields, models, api

SF = ["AGU", "BCN", "BCS", "CHH", "COL", "CMX", "DUR",
      "GRO", "GUA", "HID", "JAL", "MIC", "MOR", "MEX"]
BF = ["CAM", "COA", "CHP", "NAY"]


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.depends("user_id", "company_id", "partner_id")
    def _compute_warehouse_id(self):
        our_map = [
            (SF, "San Francisco Dealership"),
            (BF, "Buffalo Dealership"),
        ]

        for sales in self:
            stock = None
            for item in our_map:
                if sales.partner_id.state_id.code in item[0]:
                    stock = item[1]
                    break
            warehouse_id = self.env["stock.warehouse"].search(
                [("name", "=", stock)])
            if warehouse_id:
                sales.warehouse_id = warehouse_id
