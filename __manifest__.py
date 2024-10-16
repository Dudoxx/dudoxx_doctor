{
    'name': 'Dudoxx Doctor',
    'version': '16.0.1.0.0',
    'summary': 'Manage doctor profiles and API keys',
    'description': """
        This module provides functionality to manage doctor profiles
        and handle API keys for various cloud services.
    """,
    'category': 'Healthcare',
    'author': 'Walid Boudabbous, Dudoxx UG',
    'website': 'https://www.dudoxx.com',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/dudoxx_doctor_security.xml',
        'security/ir.model.access.csv',
        'views/dudoxx_doctor_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
            'dudoxx_doctor/static/src/css/dudoxx_doctor.css',
            'dudoxx_doctor/static/src/js/dudoxx_doctor_widgets.js',
        ],
    },
}