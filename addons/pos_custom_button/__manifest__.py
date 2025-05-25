# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Point of Sale Custom Button',
    'version': '1.0',
    'category': 'Sales/Point of Sale',
    'sequence': -1,
    'summary': 'Simple custom Button in the Point of Sale ',
    'description': """

This module allows you to add a custom button in the Point of Sale interface.

""",
    'depends': ['point_of_sale'],
    'data': [
        # 'data/pos_discount_data.xml',
        # 'views/res_config_settings_views.xml',
        # 'views/pos_config_views.xml',
        ],
    'installable': True,
    'assets': {
        'point_of_sale._assets_pos': [
            # 'pos_discount/static/src/**/*',
            'pos_custom_button/static/src/js/custom_button.js',
            'pos_custom_button/static/src/xml/custom_button.xml',
        ],
        'web.assets_tests': [
            # 'pos_discount/static/tests/tours/**/*',
        ],
    },
    'license': 'LGPL-3',
}
