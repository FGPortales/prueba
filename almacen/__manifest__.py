{
    'name': 'Almacén',
    'version': '0.0.1',
    'summary': 'Módulo para gestionar almacén',
    'description': """
            Módulo para administrar el almacén(listar productos, productos de entrada, productos de salida)
    """,
    'category': 'Tools',
    'author': 'Freddy Portales',
    'website': 'https://www.almacenes.com',
    'depends': ['base'],
    'data': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': '_auto_install_l10n',
}