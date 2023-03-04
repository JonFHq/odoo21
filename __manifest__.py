# -*- coding: utf-8 -*-
{
    'name': "recu",
    'summary': """Recu odoo""",
    'description': """Odoo module to buy 2nd hand laptops:""",
    'author': "Jon, Federico, Daniel",
    'website': "https://github.com/SalesianosZaragoza/recuperacion-odoo-jonfeddan",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Recuperacion',
    'version': '1.0',
    'application': True,
    'sequence': -100,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/usuario.xml',
        'views/producto.xml',
        'views/venta.xml',
        'views/menus.xml'
    ],
}
