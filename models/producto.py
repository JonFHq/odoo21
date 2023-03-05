from odoo import models, fields, api

class producto(models.Model):

    _name = "producto"
    _description = "producto"

    portatil = fields.Many2one('portatil', string='Portatil')
    precio = fields.Integer(string='Precio del producto', required=True)
    estado = fields.Selection([('0', 'Recién Fabricado'), ('1', 'Casi Nuevo'), ('2', 'Algo Desgastado'), ('3', 'Bastante Desgastado'), ('4', 'Deplorable')], string='Estado del producto', required=True)
    SO = fields.Char(string='SO', required=True)
    fechaSubida = fields.Date(string='Fecha de venta')
    vendedor = fields.Many2one('usuario', required=True)
    venta = fields.One2many('venta', 'producto', string='Venta')
