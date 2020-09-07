
{
    'name' : 'Tienda de Bicicletas',
    'version' : '0.0.1',
    'summary': 'Módulo para vender bicicletas',
    'description': """
            Módulo para administrar la venta de bicicletas
    """,
    'category': 'Sale',
    'website': 'https://www.vendobicicletas.com',
    'depends': ['base'],
    'data': [
        # Archivo de reglas de acceso
        'security/ir.model.access.csv',
        # Vistas
        'views/bicicleta_store_menus.xml',
        'views/cliente_views.xml',
        'views/bicicleta_views.xml',
        'views/vendedor_views.xml',
        'views/comprobante_pago_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    #'post_init_hook': '_auto_install_l10n',
}
