from odoo import fields, models


class Vendedor(models.Model):
    _name = 'bicicletastore.vendedor'
    _description = 'Tabla vendedor'

    name = fields.Char(string='Nombre')
    dni = fields.Char(string='DNI')
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    correo = fields.Char(string='Correo')
