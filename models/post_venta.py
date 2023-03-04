from odoo import models, fields, api

class post_venta(models.Model):

    _name = 'post_venta'
    _rec_name = 'venta'
    _description = 'post_venta'

    comprador = fields.Char(string="comprador", required=True)
    vendedor = fields.Char(string="vendedor", required=True)
    puntuacionDada = fields.Integer(string="puntuacionDada", required=True)
    mensaje = fields.Char(string="mensaje", required=True)
    venta = fields.Char(string="compañia", required=True)