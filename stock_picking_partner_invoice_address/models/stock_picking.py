# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models
# from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    partner_invoice_id = fields.Many2one(string="Invoice Address", related="sale_id.partner_invoice_id", store=True)
    same_invoiced_id = fields.Boolean(string="Partner = Invoice ", store=True, help="Whether or not the trading partner address is the same as the Invoice Address.")

    # same_invoiced_id = fields.Boolean(string="Partner Address = Invoice Address", compute='_compute_same_with_partner_invoiced_id', store=True, help="Whether or not the trading partner address is the same as the Invoice Address.")

    # @api.one
    # def _compute_same_with_partner_invoiced_id(self):
    #     # Depending on whether the partner_invoiced_id is the same or not, the data to be linked to the shipping company and the template to be used for export will be different.
    #     if not self.active or not self.is_company and self.parent_id:
    #         return
    #     self.env.cr.execute()


