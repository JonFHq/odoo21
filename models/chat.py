from odoo import _, models, fields, api

class Chat(models.Model):

    _name = "chat"
    _description = "chat"

    comprador = fields.Char(string='comprador', required=True)
    vendedor = fields.Char(string='vendedor', required=True)
    mensajes = fields.One2many('mensaje', 'chat', string='mensajes')