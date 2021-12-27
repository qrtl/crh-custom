# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    categ_id = fields.Many2one(related="product_id.categ_id", store=True)

# class SaleOrder(models.Model):
#     _inherit = "sale.order"

#     country_id = fields.Many2one(related="partner_id.country_id", store=True,)
#     country_code = fields.Char(related="partner_id.country_id.code", store=True,)
