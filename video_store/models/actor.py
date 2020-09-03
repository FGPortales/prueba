from odoo import fields, models

TIPO_DOC_SELECTION =[
    ('dni', 'DNI'),
    ('ce', 'Carnet de Extranjería')
]


class Actor(models.Model):
    _name = 'videostore.actor'
    _description = 'Tabla de Actores'

    name = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellidos')
    edad = fields.Integer(string='Edad')
    tipo_doc = fields.Selection(TIPO_DOC_SELECTION,string='Tipo doc.')
    num_doc = fields.Integer(string='Número doc.')
    direccion = fields.Char(string='Dirección')
    telefono = fields.Integer(string='Teléfono')
    # nombre, comunicacion # relacion de las clases
    line_ids = fields.One2many('videostore.pelicula.line', 'actor_id', string='peliculas')

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'El nombre no se puede repetir'),
        ('unique_num_doc', 'unique(num_doc)', 'El dni ya esta registrado'),
    ]
