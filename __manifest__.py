# -*- coding: utf-8 -*-
{
    'name': 'Message Delete',
    'version': '1.0',
    'category': 'Discuss',
    'summary': 'Administrator (SuperUser) might delete messages',
    'description': '''
The app goal is to let admins (superuser only) to remove messages. In other cases a warning appears.
    ''',
    'price': '0.00',
    'currency': 'EUR',
    'auto_install': False,
    'author': 'IT Libertas',
    'website': 'https://itlibertas.com',
    'depends': [
        'mail',
    ],
    'data': [
        'data/data.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
    ],
    'qweb': [
        'static/src/xml/message_delete.xml',
    ],
    'js': [

    ],
    'demo': [

    ],
    'test': [

    ],
    'license': 'Other proprietary',
    'images': [
        'static/description/main.png',
    ],
    'update_xml': [

    ],
    'application': True,
    'installable': True,
    'private_category': False,
    'external_dependencies': {
    },

}
