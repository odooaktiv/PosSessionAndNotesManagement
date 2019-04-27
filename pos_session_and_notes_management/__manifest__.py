# -*- coding: utf-8 -*-
{
    'name': "POS Session and Notes Management",
    'summary': """
        Manage POS Session according users and added Notes
        """,
    'description': """
    Manage POS Session according users and added Notes in KOT receipt and bill receipt.
        """,
    'version': '11.0.1.0.0',
    'author': "AktivSoftware",
    'website': "www.aktivsoftware.com",
    "category": "Point of Sale",
    'license': "AGPL-3",
    'depends': ['point_of_sale', 'pos_restaurant', 'pos_discount',
                'pos_reprint', 'pos_sale'],
    'data': [
        'security/pos_restaurant_customisation_security.xml',
        'views/pos_config_views.xml',
        'views/res_users_view.xml',
        'views/pos_templates.xml',
        'views/pos_order_line_view.xml',
    ],
    "qweb": [
        'static/src/xml/pos.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
