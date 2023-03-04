from odoo import models, fields, api

class venta(models.Model):
    _name = "venta"
    _rec_name = "nombre"
    _description = "venta"

    nombre = fields.Char(string="Registro", compute='_dependecias')
    comprador = fields.Many2one('usuario', required=True)
    vendedor = fields.Many2one('usuario', required=True)
    producto = fields.Reference('producto', 'venta')
    precio = fields.Integer(string='Precio', required=True)
    fecha_venta = fields.Date(string="Fecha de venta", required=True)
    
    @api.depends('comprador', 'vendedor', 'producto', 'fecha_venta', 'precio')
    def _dependecias(self):
        for record in self:
            record.nombre = str(record.comprador.nombre) + ' compro el producto ' + str(record.producto.nombre) + ' de ' + str(record.vendedor.nombre) + ' por ' + str(record.precio) + '€' + ' el dia ' + str(record.fecha_venta)
   
    @api.onchange('vendedor')
    def _onchange_vendedor(self):
        try:
            if self.vendedor:
                if self.vendedor.vendedor == False:
                    raise ValueError("El usuario no es vendedor")
        except:
            return {
                'warning': {
                    'title': "Error",
                    'message': "El usuario no es vendedor",
                }
            }

    @api.onchange('vendedor', 'comprador')
    def _onchange_usuario(self):
        try:
            if self.vendedor and self.comprador:
                if self.vendedor == self.comprador:
                    raise ValueError("No puede comprarse un producto a si mismo")
        except:
            return {
                'warning': {
                    'title': "Error",
                    'message': "No puede comprarse un producto a si mismo",
                }
            }

    @api.onchange('producto', 'vendedor')
    def _onchange_producto(self):
        try:
            if self.producto and self.vendedor:
                if self.producto.vendedor != self.vendedor:
                    raise ValueError("El producto no pertenece al vendedor") 
        except:
            return {
                'warning': {
                    'title': "Error",
                    'message': "El producto no pertenece al vendedor",
                }
            }

    @api.onchange('precio')
    def _onchange_precio(self):
        try:
            if self.precio:
                if self.precio <= 0:
                    raise ValueError("El precio no puede ser negativo o gratuito")
        except:
            return {
                'warning': {
                    'title': "Error",
                    'message': "El precio no puede ser negativo o gratuito",
                }
            }
