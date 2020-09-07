from odoo import api,fields, models


class Comprobante_bicicleta(models.Model):
    _name = 'bicicletastore.comprobante.bicicleta'

    name = fields.Char(string='Name')
    comprobante_id = fields.Many2one('bicicletastore.comprobantepago.cliente', required=True, string='Comprobante Pago')
    bicicleta_id = fields.Many2one('bicicletastore.bicicleta', required=True, string='Bicicleta')
    cantidad = fields.Integer(string='Cantidad')
    precio = fields.Float(string='Precio')  # (store=true)para almacenar en BD
                                      # , compute='_compute_precio', store=True
    precio_total = fields.Float(string='Precio Total')
                                                   # , compute='_compute_precio_total', store=True

    @api.depends('bicicleta_id')
    def _compute_precio(self): # este self te manda_todo el registro
        for registro in self:
            registro.precio = registro.bicicleta_id.precio

    @api.depends('precio', 'cantidad')
    def _compute_precio_total(self):
        for registro in self:
            registro.precio_total = registro.precio * registro.cantidad

    @api.onchange('bicicleta_id')
    def _onchange_bicicleta_id(self):
        # self.precio = self.bicicleta_id.precio
        return {'value': {'precio': self.bicicleta_id.precio}}

    @api.onchange('precio', 'cantidad')
    def _onchange_precio_cantidad(self):
        #self.precio_total = self.precio * self.cantidad
        return {'value': {'precio_total': self.precio * self.cantidad}}