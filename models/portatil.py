from odoo import models, fields, api

class portatil(models.Model):
    
    _name = "portatil"
    _rec_name = "nombre"
    _description = "portatil"
    
    modelo = fields.Char(string="modelo", required=True)
    imagen = fields.Image()
    resolucion = fields.Char(string="resolucion", required=True)
    frecuencia = fields.Char(string="frecuencia", required=True)
    tamaño = fields.Char(string="tamaño", required=True)
    peso = fields.Char(string="peso", required=True)
    RAM = fields.Integer(string="RAM", required=True)
    HDD = fields.Integer(string="HDD", required=True)
    SSD = fields.Integer(string="SSD", required=True)
    grafica = fields.Char(string="grafica", required=True)
    USB3 = fields.Integer(string="USB 3.0", required=True)
    USB2 = fields.Integer(string="USB 2.0", required=True)
    placa_base = fields.Char(string="placa_base", required=True)
    lector_discos = fields.Boolean(string="lector_discos", required=True)
    tactil = fields.Boolean(string="tactil", required=True)
    tablet = fields.Boolean(string="tablet", required=True)
    wifi = fields.Boolean(string="wifi", required=True)
    cable_red = fields.Boolean(string="cable_red", required=True)
    bluetooth = fields.Boolean(string="bluetooth", required=True)
    HDMI = fields.Boolean(string="HDMI", required=True)
    VGA = fields.Boolean(string="VGA", required=True)
    DPORT = fields.Boolean(string="DPORT", required=True)
    miniDPORT = fields.Boolean(string="miniDPORT", required=True)
    thunderbolt = fields.Integer(string="thunderbolt", required=True)
    jack = fields.Boolean(string="jack 3.5", required=True)
    SIM = fields.Boolean(string="SIM", required=True)
    cantidad = fields.Integer(string="cantidad", required=True)
    marca = fields.Boolean(string="marca", required=True)
    
    productos = fields.One2many('producto', 'portatil')