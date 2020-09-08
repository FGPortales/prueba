from odoo import api, fields, models
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
    total_todo = fields.Float(string='Total', compute='_compute_total_todo', store=True)
    saldo = fields.Float(string='Saldo', compute='_compute_saldo',store=True)
    historico = fields.One2many('bicicletastore.comprobantepago.historico', 'comprobantef_id', string='Historico')
    estado = fields.Char(string="Estado")#, compute='_compute_estado',store=True)



    @api.depends('linea_ids')
    def _compute_total_todo(self):
        temp = 0
        for reg in self.linea_ids:
            temp = temp + reg.precio_total
        self.total_todo = temp
        self.saldo = self.total_todo

    @api.onchange('fecha_emision','fecha_vencimiento')
    def _onchange_estado(self):
        if self.fecha_emision > self.fecha_vencimiento:
            self.estado = 'Vencido'
        elif self.fecha_emision < self.fecha_vencimiento:
            self.estado = 'Pendiente '
        else:
            self.estado = 'Hoy'

    @api.depends('historico')
    def _compute_saldo(self):
        m = 0
        band = 1
        for reg in self.historico:
            m = m + reg.monto
        self.saldo = self.total_todo - m




