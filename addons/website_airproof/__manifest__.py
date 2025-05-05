{
   'name': 'Airproof Theme',
   'description': 'This is website theme for Airproof',
   'category': 'Theme',
   'sequence': 20,
   'version': '18.0.1.0.0',
   'author': 'Bhupendra Kumar Sah',
   'license': 'LGPL-3',
   'depends': ['website'],
   'data': [
      'data/website.xml',
      'views/custom_header.xml',
      'views/hero_section.xml',
      'views/layout.xml',
      'views/custom_footer.xml',
   ],
   'assets': {
      'web._assets_primary_variables': [
      'website_airproof/static/src/scss/primary_variables.scss',
   ],
   #    'web._assets_frontend_helpers': [
   #    ('prepend', 'website_airproof/static/src/scss/bootstrap_overridden.scss'),
   # ],
   'web.assets_frontend': [
      'website_airproof/static/src/scss/theme.scss',
      'website_airproof/static/src/js/theme.js',
   ],

   },
    "installable": True,
    "application": True,
}