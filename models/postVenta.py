from odoo import models, fields, api

class postVenta(models.Model):

    _name = "postVenta"
    _rec_name = "nombre"
    _description = "postVenta"

    comprador = fields.Char(string="comprador", required=True)
    vendedor = fields.Char(string="vendedor", required=True)
    puntuacionDada = fields.Integer(string="puntuacionDada", required=True)
    mensaje = fields.Char(string="mensaje", required=True)
    venta = fields.Char(string="compañia", required=True)