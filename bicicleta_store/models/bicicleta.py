from odoo import api,fields, models

class Bicicleta(models.Model):
    _name = 'bicicletastore.bicicleta'

    name = fields.Char(string='Nombre')
    precio = fields.Float(string='Precio')
    marca = fields.Char(string='Marca')
    modelo = fields.Char(string="Modelo")
    linea_ids = fields.One2many('bicicletastore.comprobante.bicicleta', 'bicicleta_id', string='Bicicleta')

