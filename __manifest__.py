# -*- coding: utf-8 -*-
{
    'name': "lib_custom",

    'summary': """
        + Custom Field and Modification""",

    'description': """
        + Adding field to module "Pisau Plong"
    """,

    'author': "Satusoft",
    'website': "https://satusoft.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Custom Addon',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','openeducat_library'],

    # always loaded
    'data': [
#        'security/ir.model.access.csv',
        'views/views.xml'
    ],
    
}
