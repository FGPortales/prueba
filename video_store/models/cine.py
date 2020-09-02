from odoo import fields, models

class Cine(models.Model):
    _name = 'videostore.cine'
    _description = 'Tabla de cines'

    name = fields.Char(string='Nombre')
    direccion = fields.Char(stirng='Duracion')
    capacidad = fields.Integer(string='Capacidaad')
    pel_cin = fields.One2many('videostore.pelicula.cine', 'cinec_id', string='Peliculas')