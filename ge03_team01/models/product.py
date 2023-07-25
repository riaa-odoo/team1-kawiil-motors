from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    name = fields.Char("Name", index="trigram", translate=True, compute="_compute_name", store=True, readonly=False)

    @api.depends("make", "model", "year")
    def _compute_name(self):
        domain = [('detailed_type', 'like', 'motorcycle')]
        for template in self.search(domain):
            template.name = f"{template.year} {template.make} {template.model}"
