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

    @api.multi
    @api.depends("partner_id", "partner_invoice_id")
    def _compute_is_identical_partners(self):
        for pick in self:
            if pick.partner_id == pick.partner_invoice_id:
                pick.is_identical_partners = True
