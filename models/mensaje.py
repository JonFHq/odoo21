from odoo import models, fields, api

class chat(models.Model):

    _name = "chat"
    _rec_name = "nombre"
    _description = "chat"

    comprador = fields.Char(string="comprador", required=True)
    vendedor = fields.Char(string="vendedor", required=True)
    texto = fields.Char(string="texto", required=True)
    fecha = fields.Date(string="fecha", required=True)
    chat = fields.Char(string="chat", required=True)
    usuario = fields.Char(string="usuario", required=True)
    