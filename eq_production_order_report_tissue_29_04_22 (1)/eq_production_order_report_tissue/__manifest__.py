# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2019 EquickERP
#
##############################################################################
{
    'name': "Production Order Report",
    'category': 'Manufacturing',
    'version': '15.0.1.0',
    'author': 'Equick ERP',
    'description': """
        Production Order Report.
    """,
    'summary': """Production Order Report""",
    'depends': ['mrp'],
    'license': 'OPL-1',
    'website': "",
    'data': [
        'views/mrp_production_view.xml',
        'report/mrp_production_templates.xml'
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
