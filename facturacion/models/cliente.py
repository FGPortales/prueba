from odoo import api, fields, models


class Cliente(models.Model):
    _name = 'facturacion.cliente'
    _description = 'tabla de clientes'

    name = fields.Char(string='Nombre')
    apellidos = fields.Char(string='Apellido')
    dni = fields.Integer(string='DNI')
    direccion = fields.Char(string='Direccion')
    telefono = fields.Char(string='Telefono')
    email = fields.Char(string="Correo Electronico")

    # @api.onchange('dni')
    # def _onchange_dni(self):
    #     dni_value = self.dni
    #     try:
    #         int(dni_value)
    #     except:
    #         raise SyntaxError("Dni debe ser número")


