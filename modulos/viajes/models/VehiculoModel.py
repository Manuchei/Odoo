from odoo import models, fields, api


class Vehiculo(models.Model):
    _inerits = 'producto'
    _name = 'viajes.vehiculo'
    _description = "viajes Vehiculo"
    modelo = fields.Char(string="Modelo", required=True)
    marca = fields.Char(string="Marca")
    descripcion = fields.Text()
