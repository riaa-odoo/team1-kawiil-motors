from odoo import api, models, fields
from odoo.exceptions import ValidationError


class MotorcycleRegistry(models.Model):
    _inherit = "motorcycle.registry"

    lot_ids = fields.One2many("stock.lot", "registry_id", string="Lot IDs")
    lot_id = fields.Many2one("stock.lot", string="Lot ID", compute="_compute_lot_id")
    sale_order_id = fields.Many2one("sale.order")
    owner_id = fields.Many2one("res.partner", string="Owner", related="sale_order_id.partner_id")
    registry_date = fields.Date(string='Registration Date', default=fields.Date.today())

    @api.constrains("lot_ids")
    def _check_lot_ids(self):
        for registry in self:
            if len(registry.lot_ids) > 1:
                raise ValidationError("lot_ids cannot have more than one lot.")

    @api.depends("lot_ids")
    def _compute_lot_id(self):
        self.lot_id = ""
        for registry in self.filtered(lambda r: r.lot_ids is not False and len(r.lot_ids) > 0):
            registry.lot_id = registry.lot_ids[0]

    def action_view_sale_order(self):
        action = self.env['ir.actions.act_window']._for_xml_id('sale.action_orders')
        action["views"] = [(False, 'form')]
        action["res_id"] = self.sale_order_id.id
        return action
