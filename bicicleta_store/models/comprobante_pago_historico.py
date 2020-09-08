from odoo import fields, models


class Comprobantepago_historico(models.Model):
    _name = 'bicicletastore.comprobantepago.historico'

    name = fields.Char(string='Name')
    comprobantef_id = fields.Many2one('bicicletastore.comprobantepago.cliente',string='Comprobante ID')
    fecha = fields.Date(string='Fecha')
    monto = fields.Float(string='Monto')
