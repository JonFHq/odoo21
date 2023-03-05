from odoo import models, fields, api

class post_venta(models.Model):

    _name = 'post_venta'
    _rec_name = 'venta'
    _description = 'post_venta'

    comprador = fields.Many2one('usuario', required=True)
    vendedor = fields.Many2one('usuario', required=True)
    puntuacionDada = fields.Integer(string="puntuacionDada", required=True)
    mensaje = fields.Char(string="mensaje", required=True)
    venta = fields.Char(string="compañia", required=True)