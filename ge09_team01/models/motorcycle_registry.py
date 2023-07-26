from odoo import api, fields, models


class MotorcycleRegistry(models.Model):
    _inherit = "motorcycle.registry"

    repair_order_ids = fields.One2many(
        "repair.order", inverse_name="registry_id")
    count_orders = fields.Integer(compute='_count_orders')

    def action_view_repair_order(self):
        self.ensure_one()
        action = self.env['ir.actions.act_window']._for_xml_id(
            'repair.action_repair_order_tree')
        action['domain'] = [('registry_id', '=', self.id)]
        return action

    @api.depends('repair_order_ids')
    def _count_orders(self):
        self.count_orders = len(self.repair_order_ids)
