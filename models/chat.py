from odoo import models, fields, api

class chat(models.Model):

    _name = "chat"
    _rec_name = "nombre"
    _description = "chat"

    comprador = fields.Char(string="comprador", required=True)
    vendedor = fields.Char(string="vendedor", required=True)
    mensaje = fields.Char(string="mensaje", required=True)