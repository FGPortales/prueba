from odoo import fields, models


class ComprobantePagoCliente(models.Model):
    _name = 'bicicletastore.comprobantepago.cliente'
    _description = 'Comprobante de pago de cliente'
    _order = 'name'  # ordenar alfabeticamente segun el nombre

    name = fields.Char(string='Serie-Correlativo')
    fecha_emision = fields.Date(string='Fecha de Emisión')
    fecha_vencimiento = fields.Date(string='Fecha de vencimiento')
    cliente_id = fields.Many2one('bicicletastore.cliente', string="Cliente")
    vendedor_id = fields.Many2one('bicicletastore.vendedor', string="Vendedor")