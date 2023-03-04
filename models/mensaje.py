from odoo import _, api, fields, models

class Mensaje(models.Model):

    _name = 'mensaje'
    _rec_name = 'texto'
    _description = 'mensaje'

    comprador = fields.Char(string="comprador", required=True)
    vendedor = fields.Char(string="vendedor", required=True)
    texto = fields.Char(string="texto", required=True)
    fecha = fields.Date(string="fecha", required=True)
    chat = fields.Char(string="chat", required=True)
    usuario = fields.Char(string="usuario", required=True)
    