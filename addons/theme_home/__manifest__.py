# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Home Page Theme',
    'description': 'Home Page website theme',
    'category': 'Theme',
    'sequence': 10,
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'views/header.xml',
        'views/hero.xml',
        'views/footer.xml',
    ],
    'assets': {
    'web.assets_frontend': [
        'theme_home/static/src/css/custom_header.css',
        'theme_home/static/src/css/custom_hero.css',
        'theme_home/static/src/css/custom_footer.css',
    ],
    },
    'images': [],
    'license': 'LGPL-3',
}
