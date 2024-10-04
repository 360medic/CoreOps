{
    'name': 'Custom MRP Module',
    'version': '1.0',
    'category': 'Manufacturing',
    'summary': 'Custom module to load MRP demo data',
    'description': """
        This module adds custom demo data for the MRP (Manufacturing) module, including
        Bill of Materials, Work Centers, and Production Orders.
    """,
    'depends': ['mrp'],
    'data': [
        'data/mrp_verifier.xml',
    ],
    'installable': True,
    'auto_install': False,
}
