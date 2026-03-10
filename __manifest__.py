{
    'name': 'Customer Equipment Management',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'summary': 'Mencatat peralatan customer dan riwayat servicenya',
    'description': """
        Modul untuk mencatat peralatan (equipment) yang dimiliki customer 
        beserta riwayat perbaikannya (service history).
    """,
    'author': 'Hajril',
    'depends': ['base', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/equipment_views.xml',
        'views/services_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}