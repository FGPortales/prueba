from odoo import fields, models


class Cliente(models.Model):
    _name = 'bicicletastore.cliente'
    _description = 'Tabla cliente'

    name = fields.Char(string='Nombre', required=True, help='Debe poner algo')
    direccion = fields.Char(string='Dirección')