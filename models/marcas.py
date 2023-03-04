from odoo import models, fields, api

class marcas(models.Model):

    _name = "marcas"
    _rec_name = "nombre"
    _description = "marcas"

    nombre = fields.Char(string="nombre", required=True)