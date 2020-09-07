from odoo import fields, models
from datetime import datetime


TerminoPago_Selection = [
    ('contado', 'Al contado'),
    ('plazo15', '15 días plazo'),
    ('plazo30', '30 días plazo'),
    ('fraccionado2', 'fraccionado en 2 partes')
]

Moneda_Selection = [
    ('soles', 'Soles'),
    ('dolares', 'Dolares'),
    ('euros', 'Euros')
]

class ComprobantePagoCliente(models.Model):
    _name = 'bicicletastore.comprobantepago.cliente'
    _description = 'Comprobante de pago de cliente'
    _order = 'name'  # ordenar alfabeticamente segun el nombre

    name = fields.Char(string='Serie-Correlativo')
    tipo = fields.Selection([('boleta', 'Boleta'), ('factura', 'Factura')], string='Tipo de Comprobante')
    fecha_emision = fields.Date(string='Fecha de Emisión', default=datetime.today())
    fecha_vencimiento = fields.Date(string='Fecha Vencimiento')
    terminos_pago = fields.Selection(TerminoPago_Selection, string='Términos de Pago')
    moneda = fields.Selection(Moneda_Selection, string='Moneda')
    cliente_id = fields.Many2one('bicicletastore.cliente', string="Cliente")
    vendedor_id = fields.Many2one('bicicletastore.vendedor', string="Vendedor")
    linea_ids = fields.One2many('bicicletastore.comprobante.bicicleta', 'comprobante_id', string='Comprobante')
