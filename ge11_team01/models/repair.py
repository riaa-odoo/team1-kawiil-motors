from odoo import api, fields, models


class RepairOrder(models.Model):
    _name = "repair.order"
    _inherit = ["repair.order", "portal.mixin"]

    is_public = fields.Boolean("Public", default=True)

    def _get_order_portal_return_action(self):
        self.ensure_one()
        return self.env.ref("repair.stock_production_lot_view_form")

    def _compute_access_url(self):
        for order in self:
            order.access_url = f"/repairorder/{order.id}"

    def _set_is_public(self):
        self.ensure_one()
        self.is_public = not self.is_public
