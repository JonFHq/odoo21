from odoo import _, models, fields, api

class Chat(models.Model):

    _name = "chat"
    _description = "chat"

    usuarios = fields.Many2many('usuario', string='Destinatarios')
    mensajes = fields.One2many('mensaje', 'chat', string='Mensajes')
