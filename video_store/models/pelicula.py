from odoo import fields, models


GENERO_SELECTION = [
    ('terror','Terror'),
    ('horror','Horror'),
    ('comedio','Comedia'),
    ('suspenso','Suspenso'),
    ('drama','Drama')
]

class Pelicula(models.Model):
    _name = 'videostore.pelicula'
    _description = 'Tabla de Películas'

    name = fields.Char(string='Nombre', required=True)
    duracion = fields.Char(string='Duración')
    director = fields.Char(string='Nombre Director', required=True)
    anio_lanzamiento = fields.Char(stirng='Año lanzamiento')
    genero = fields.Selection(GENERO_SELECTION,string='Género')
    numero = fields.Integer(string='Número')
    resenia = fields.Text(string='Reseña')


