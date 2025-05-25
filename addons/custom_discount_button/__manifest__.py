# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'custom_discount_pos_btn',
    'version': '1.0.2',
    'category': 'Point of Sale',
    'summary': 'Adds Discount Button to POS',
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            'custom_discount_button/static/js/discount_button.js',
            'custom_discount_button/static/xml/discount_button.xml',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}