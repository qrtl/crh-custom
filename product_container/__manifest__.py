# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Product Container',
    'summary': '',
    'description': """
Adds Container field to product.
    """,
    'version': '12.0.1.0.0',
    'category': 'Product',
    'website': 'https://www.quartile.co/',
    'author': 'Quartile Limited',
    'license': 'AGPL-3',
    'installable': True,
    'depends': [
        'product',
    ],
    'data': [
        'views/product_views.xml',
    ],
}
