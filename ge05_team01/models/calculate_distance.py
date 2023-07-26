from odoo import api, fields, models

san_francisco = ["California", "Oregon", "Washington",
                 "Nevada", "Arizona", "Utah", "Idaho", "Montana", "Wyoming", "Colorado", "New Mexico", "Sonora", "Sinaloa", "Nayarit", "Baja California", "Baja California Sur"]
buffalo = ["New York", "Pennsylvania", "Ohio", "Michigan", "Indiana", "West Virginia", "Vermont",
           "New Hampshire", "Maine", "Massachusetts", "Rhode Island", "Connecticut", "Delaware", "Maryland", "Tamaulipas", "Nuevo Leon", "Coahuila", "Chihuahua", "Durango", "Zacatecas", "San Luis Potosi", "Aguascalientes", "Jalisco"]


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.depends("user_id", "company_id", "partner_id")
    def _compute_warehouse_id(self):
        for order in self:
            if order.partner_id.state_id.name in san_francisco:
                order.warehouse_id = self.env["stock.warehouse"].search(
                    [("name", "=", "San Francisco Dealership")])
            elif order.partner_id.state_id.name in buffalo:
                order.warehouse_id = self.env["stock.warehouse"].search(
                    [("name", "=", "Buffalo Dealership")])
            else:
                return super()._compute_warehouse_id()
