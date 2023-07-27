from odoo import http, _
from odoo.addons.portal.controllers import portal
from odoo.exceptions import AccessError, MissingError
from odoo.http import request

from odoo.addons.portal.controllers.portal import pager as portal_pager
from odoo.osv.expression import OR


class PortalMotorcycleRegistry(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)

        MotorcycleRegistry = request.env["motorcycle.registry"]
        if "registry_count" in counters:
            values["registry_count"] = MotorcycleRegistry.search_count(
                [("owner_id", "=", request.env.user.partner_id.id)]) if MotorcycleRegistry.check_access_rights(
                "read", raise_exception=False) else 0
        return values

    def _prepare_motorcycle_registry_portal_rendering_values(
            self, page=1, sortby=None, search_in="all", search=None, **kwargs):
        MotorcycleRegistry = request.env["motorcycle.registry"]

        if not sortby:
            sortby = "registry_number"

        domain = ["|", ("owner_id", "=", request.env.user.partner_id.id), ("is_public", "=", "True")]
        url = "/my/registries"
        values = self._prepare_portal_layout_values()

        searchbar_sortings = self._get_registry_searchbar_sortings()
        searchbar_inputs = self._get_registry_searchbar_inputs()
        sort_order = searchbar_sortings[sortby]["order"]

        pager_values = portal_pager(
            url=url,
            total=MotorcycleRegistry.search_count(domain),
            page=page,
            step=self._items_per_page,
            url_args={"sortby": sortby, "search_in": search_in, "search": search}
        )

        if search and search_in:
            domain += self._get_search_domain(search_in, search)

        registries = MotorcycleRegistry.search(
            domain, order=sort_order, limit=self._items_per_page, offset=pager_values['offset'])

        values.update({
            "registries": registries.sudo(),
            "page_name": "motorcycle_registry",
            "pager": pager_values,
            "default_url": url,
            "searchbar_inputs": searchbar_inputs,
            "searchbar_sortings": searchbar_sortings,
            "search": search,
            "search_in": search_in,
            "sortby": sortby,
        })

        return values

    def _get_registry_searchbar_inputs(self):
        return {
            'all': {'input': 'all', 'label': _('Search All')},
            'name': {'input': 'name', 'label': _('Search by Name')},
            'country': {'input': 'country', 'label': _('Search by Country')},
            'state': {'input': 'state', 'label': _('Search by State')},
        }

    def _get_registry_searchbar_sortings(self):
        return {
            'registry_number': {'label': _('ID'), 'order': 'registry_number desc'},
            'name': {'label': _('Owner name'), 'order': 'owner_id desc'},
            'model': {'label': _('Model'), 'order': 'model asc'},
            'make': {'label': _('Brand'), 'order': 'make'},
            'mileage': {'label': _('Road Experience'), 'order': 'current_mileage desc'},
            'lp': {'label': _('License Plate'), 'order': 'license_plate asc'},
        }

    def _get_search_domain(self, search_in, search):
        search_domain = []
        if search_in in ('name', 'all'):
            search_domain = OR([search_domain, [('owner_id', 'ilike', search)]])
        if search_in in ('country', 'all'):
            search_domain = OR([search_domain, [('owner_id.country_id', 'ilike', search)]])
        if search_in in ('state', 'all'):
            search_domain = OR([search_domain, [('owner_id.state_id', 'ilike', search)]])

        return search_domain

    @http.route("/my/registries", type="http", auth="user", website=True)
    def portal_my_registries(self, **kwargs):
        values = self._prepare_motorcycle_registry_portal_rendering_values(**kwargs)
        return http.request.render("ge08_team01.portal_my_motorcycle_registries_list", values)

    @http.route(["/my/registries/<int:registry_id>"], type="http", auth="public", website=True)
    def portal_registry_page(self, registry_id, access_token=None):
        try:
            registry_sudo = self._document_check_access("motorcycle.registry", registry_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect("/my")

        backend_url = f"/web#model={registry_sudo._name}"\
                      f"&id={registry_sudo.id}"\
                      f"&action={registry_sudo._get_portal_return_action().id}"\
                      f"&view_type=form"

        values = {
            "registry": registry_sudo,
            "report_type": "html",
            "backend_url": backend_url
        }

        values = self._get_page_view_values(registry_sudo, access_token, values, "my_registrations_history", False)
        return request.render("ge08_team01.motorcycle_registry_portal_template", values)
