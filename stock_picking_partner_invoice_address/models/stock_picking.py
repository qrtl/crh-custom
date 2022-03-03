# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models

# from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    partner_invoice_id = fields.Many2one(
        string="Invoice Address", related="sale_id.partner_invoice_id", store=True
    )
    is_identical_partners = fields.Boolean(
        string="PartnerAdd = InvoiceAdd",
        compute="_compute_is_identical_partners",
        store=True,
        help="Whether or not the trading partner address is the same as the Invoice Address.",
    )

    @api.one
    # test-compute 1
    def _compute_is_identical_partners(self):
        # Depending on whether the partner_invoiced_id is the same or not, the data to be linked to the shipping company and the template to be used for export will be different.
        if not self.active or not self.is_identical_partners and self.partner_id:
            return
        stock_picking.is_identical_partners = True

    # 参考
    # if not self.active or not self.is_company and self.parent_id:
    #     return
    # self.env.cr.execute()

    # test-compute 2
    # def _compute_is_identical_partners(self):
    #     for stock_picking in self:
    #         stock_picking.is_identical_partners = True

    # 参考
    # def _compute_is_product_variant(self):
    #     for product in self:
    #         product.is_product_variant = True

    # test-change view dipends on picking_type_id
    # @api.model
    # def fields_view_get(
    #     self, view_id=None, view_type="form", toolbar=False, submenu=False
    # ):
    #     if view_type == "tree":
    #         pick_type_id = self._context.get("default_picking_type_id")
    #         if (
    #             not pick_type_id
    #             or pick_type_id
    #             and self.env["stock.picking.type"].browse([pick_type_id]).code
    #             in "outgoing"
    #         ):
    #             view_id = self.env.ref(
    #                 "stock_picking_partner_invoice_address.vpicktree_outgoing"
    #             ).id
    #     return super(StockPicking, self).fields_view_get(
    #         view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu
    #     )
