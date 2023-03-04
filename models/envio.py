from odoo import models, fields, api

class envio(models.Model):

    _name = "envio"
    _rec_name = "nombre"
    _description = "envio"

    venta = fields.Char(string="venta", required=True)
    origen = fields.Char(string="origen", required=True)
    destino = fields.Char(string="destino", required=True)
    estado = fields.Selection(([('Pago Aceptado'),('En Preparacion'),('En Reparto'),('Pedido Recogido')]))
    compañia = fields.Char(string="compañia", required=True)