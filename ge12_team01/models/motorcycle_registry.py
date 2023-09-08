from odoo import api, models, _
from odoo.exceptions import UserError

class MotorcycleRegistry(models.Model):
    _inherit = 'motorcycle.registry'

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        data = self.env['res.users'].search([]).mapped('login')

        if res and res.wner_id:
            if res.owner_id.email not in data:
                user = self.env['res.users'].create({
                    'name': res.owner_id.name,
                    'login': res.owner_id.email,
                    'email': res.owner_id.email,
                    'partner_id': res.owner_id.id,
                })
                
                is_portal = False

                self.action_grant_access(user, is_portal)
        
        return res
    
    def action_grant_access(self, user, is_portal):
        user.ensure_one()
       
        group_portal = self.env.ref('base.group_portal')
        group_user = self.env.ref('base.group_user')

        user_sudo = user.user_id.sudo()

        if not user_sudo.active or not is_portal:
            user_sudo.write({'active': True, 'groups_id': [(4, group_portal.id), (3, group_user.id)]})
            user_sudo.partner_id.signup_prepare()

        self._send_email(user)

        return True
    
    def _send_email(self, user):
        user.ensure_one()

        template = self.env.ref('ge12_team01.mail_template_data_portal_welcome_motorcycle_registry')
        if not template:
            raise UserError(_('The template "Portal: new user" not found for sending email to the portal user.'))

        lang = user.sudo().lang
        partner = user.sudo().partner_id

        portal_url = partner.with_context(signup_force_type_in_url='', lang=lang)._get_signup_url_for_action()[partner.id]
        partner.signup_prepare()
        template.with_context(dbname=self._cr.dbname, portal_url=portal_url, lang=lang).send_mail(user.id, force_send=True)

        return True
    