from odoo import models


class Picking(models.Model):
    _inherit = "stock.picking"

    def button_validate(self):
        return super().button_validate()
