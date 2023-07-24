from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    name = fields.Char("Name", index="trigram", required=True, translate=True, compute="_compute_name")

    @api.depends("make", "model", "year")
    def _compute_name(self):
        for record in self:
            if record.detailed_type is not None and record.detailed_type == "motorcycle":
                # Check if year, make and model fields have been set
                if False not in (record.year, record.make, record.model):
                    record.name = f"{record.year} {record.make} {record.model}"
