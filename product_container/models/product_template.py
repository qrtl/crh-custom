# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    container = fields.Selection([
        ('bottle', 'Bottle'),
        ('keg', 'Keg')
        ], help="The value will be used in liquor tax reporting.")
