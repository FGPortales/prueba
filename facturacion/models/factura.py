from odoo import fields, models

class Factura(models.Model):
    _name = 'facturacion.factura'
    _description = 'Tabla de facturas'

    numeroBoleta = fields.Integer("Bolesta N°")
    nombreCliente = fields.Char(string="cliente")
    fecha = fields.Char(string="Fecha")
    total = fields.Float(string="Total")
    detalles = fields.Text(string="Detalles")
    enviarCorreo = fields.Boolean(String="Enviar factura al correo?")

