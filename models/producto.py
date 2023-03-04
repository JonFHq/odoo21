from odoo import models, fields, api

class producto(models.Model):

    _name = "producto"
    _rec_name = "nombre"
    _description = "producto"

    precio = fields.Integer(string="Precio del producto")
    estado = fields.Selection([('Recién Fabricado'),('Casi Nuevo'),('Algo Desgastado'),('Bastante Desgastado'),('Deplorable')])
    SO = fields.Char(string="SO", required=True)
    fechaSubida = fields.Date(string="Fecha de venta", required=True)
    vendedor = fields.Many2one('usuario', required=True)
    venta = fields.Reference('venta', 'producto')
    portatil = fields.Many2one('portatil', string='portatil')
    
    @api.depends('vendedor')
    def _vendido(self):
        for record in self:
            for venta in record.vendedor.venta:
                if venta.producto == self:
                    record.vendido = True
                else:
                    record.vendido = False
