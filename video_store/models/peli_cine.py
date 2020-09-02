from odoo import api,fields, models

class PeliculaCine(models.Model):
    _name = 'videostore.pelicula.cine'
    _description = 'Peliculas por cine'

    name = fields.Char(string="Name", compute='_compute_name')
    peliculac_id = fields.Many2one('videostore.pelicula', string='Pelicula')
    cinec_id = fields.Many2one('videostore.cine', string='Cine')
    fecha_estreno = fields.Char(string="Fecha de Estreno")

    @api.depends('peliculac_id', 'cinec_id')
    def _compute_name(self):
        if self.peliculac_id and self.cinec_id:
            self.name = '{} {}'.format(self.peliculac_id.name, self.cinec_id.name)
        else:
            self.name = ''

