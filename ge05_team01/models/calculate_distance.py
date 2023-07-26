from odoo import fields, models, api

san_francisco = ["California", "Oregon", "Washington",
                 "Nevada", "Arizona", "Utah", "Idaho", "Montana", "Wyoming", "Colorado", "New Mexico", "Sonora", "Sinaloa", "Nayarit", "Baja California", "Baja California Sur"]
buffalo = ["New York", "Pennsylvania", "Ohio", "Michigan", "Indiana", "West Virginia", "Vermont",
           "New Hampshire", "Maine", "Massachusetts", "Rhode Island", "Connecticut", "Delaware", "Maryland", "Tamaulipas", "Nuevo Leon", "Coahuila", "Chihuahua", "Durango", "Zacatecas", "San Luis Potosi", "Aguascalientes", "Jalisco"]


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.depends("user_id", "company_id", "partner_id")
    def _compute_warehouse_id(self):
        our_warehouses = [
            (san_francisco, "San Francisco Dealership"),
            (buffalo, "Buffalo Dealership"),
        ]

        for sales in self:
            for item in our_warehouses:
                if sales.partner_id.state_id.name in item[0]:
                    warehouse_id = self.env["stock.warehouse"].search(
                        [("name", "=", item[1])])
                    break
                else:
                    warehouse_id = self.env["stock.warehouse"].search(
                        [("id", "=", "1")])

            if warehouse_id:
                sales.warehouse_id = warehouse_id
