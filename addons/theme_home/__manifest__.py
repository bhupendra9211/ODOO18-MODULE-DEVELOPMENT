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
        'views/order-online_page.xml',
        'views/menus.xml',
        'views/snippets/reservation.xml',
        'views/snippets/snippets.xml',
    ],
    'assets': {
    # 'web._assets_primary_variables':[
    #     'theme_home/static/src/scss/primary_variables.scss',
    # ],
    'web.assets_frontend': [
        'theme_home/static/src/css/custom_header.css',
        'theme_home/static/src/css/custom_hero.css',
        'theme_home/static/src/css/custom_footer.css',
        'theme_home/static/src/css/custom_menus.css',
        'theme_home/static/src/css/style.css',
        # 'theme_home/static/src/scss/styles.scss',
    ],

    },
    'images': [],
    'license': 'LGPL-3',
    "installable": True,
    "application": True,
}
