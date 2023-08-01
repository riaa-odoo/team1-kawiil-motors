from odoo import http, _
from odoo.addons.portal.controllers import portal
from odoo.exceptions import AccessError, MissingError, UserError
from odoo.http import request

from odoo.addons.portal.controllers.portal import pager as portal_pager
from odoo.osv.expression import OR


class PortalRepairOrder(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)

        RepairOrder = request.env["repair.order"]
        if "repair_count" in counters:
            values["repair_count"] = RepairOrder.search_count([])
            values["create_count"] = "New!"
        return values

    def _prepare_repair_order_portal_rendering_values(self, page=1, sortby=None, search_in="all", search=None, **kwargs):
        RepairOrder = request.env["repair.order"]

        if not sortby:
            sortby = "registry_id"

        domain = []
        url = "/repair-order/list"
        values = self._prepare_portal_layout_values()

        searchbar_inputs = self._get_registry_searchbar_inputs()

        pager_values = portal_pager(
            url=url,
            total=RepairOrder.search_count(domain),
            page=page,
            step=self._items_per_page,
            url_args={"sortby": sortby,
                      "search_in": search_in, "search": search}
        )

        if search and search_in:
            domain += self._get_search_domain(search_in, search)

        orders = RepairOrder.search(
            domain, limit=self._items_per_page, offset=pager_values['offset'])

        values.update({
            "orders": orders.sudo(),
            "page_name": "repair_order",
            "pager": pager_values,
            "default_url": url,
            "searchbar_inputs": searchbar_inputs,
            "search": search,
            "search_in": search_in,
            "sortby": sortby,
        })

        return values

    def _prepare_create_order_portal_rendering_values(self, page=1, sortby=None, search_in="all", search=None, **kwargs):
        RepairOrder = request.env["repair.order"]

        domain = []
        url = "/repair-order/list"
        values = self._prepare_portal_layout_values()

        pager_values = portal_pager(
            url=url,
            total=RepairOrder.search_count(domain),
            page=page,
            step=self._items_per_page,
            url_args={"sortby": sortby,
                      "search_in": search_in, "search": search}
        )

        orders = RepairOrder.search(
            domain, limit=self._items_per_page, offset=pager_values['offset'])

        values.update({
            "orders": orders.sudo(),
            "page_name": "repair_order",
            "pager": pager_values,
            "default_url": url,
            "search": search,
            "search_in": search_in,
            "sortby": sortby,
        })

        return values

    @http.route("/repair-order/list", type="http", auth="user", website=True)
    def portal_my_repair_orders(self, **kwargs):
        values = self._prepare_repair_order_portal_rendering_values(
            **kwargs)
        return http.request.render("ge11_team01.portal_my_repair_order_list", values)

    @http.route("/new-order/", type="http", auth="user", website=True)
    def portal_my_create_orders(self, **kwargs):
        values = self._prepare_create_order_portal_rendering_values(
            **kwargs)
        return http.request.render("ge11_team01.portal_my_new_repair_order_list", values)

    @http.route(['/new-order/submit'], type='http', auth="public", website=True)
    def customer_form_submit(self, **post):
        try:
            request.env['repair.order'].create({
                'vin': post.get('vin'),
                'description': post.get('description'),
            })
        except:
            raise UserError(
                "Odoopsy! That VIN doesn't exist in our registries, enter a valid one! :)")
        return request.render("portal.portal_my_home")

    def _get_registry_searchbar_inputs(self):
        return {
            'all': {'input': 'all', 'label': _('Search All')},
            'ticket': {'input': 'ticket', 'label': _('Search by Ticket')},
            'vin': {'input': 'vin', 'label': _('Search by VIN')},
        }

    def _get_search_domain(self, search_in, search):
        search_domain = []
        if search_in in ('ticket', 'all'):
            search_domain = OR(
                [search_domain, [('name', 'ilike', search)]])
        if search_in in ('vin', 'all'):
            search_domain = OR(
                [search_domain, [('vin', 'ilike', search)]])
        return search_domain

    @http.route(["/repairorder/<int:id>"], type="http", auth="public", website=True)
    def portal_order_page(self, id, access_token=None):
        try:
            order_sudo = self._document_check_access(
                "repair.order", id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect("/repair-order/list")

        backend_url = f"/web#model={order_sudo._name}"\
                      f"&id={order_sudo.id}"\
                      f"&action={order_sudo._get_order_portal_return_action().id}"\
                      f"&view_type=form"

        values = {
            "repair_order": order_sudo,
            "report_type": "html",
            "backend_url": backend_url
        }

        values = self._get_page_view_values(
            order_sudo, access_token, values, "my_registrations_history", False)
        return request.render("ge11_team01.repair_order_portal_template", values)
