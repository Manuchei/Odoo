from odoo import models, fields, api
from datetime import timedelta


class Viaje(models.Model):
    _name = 'viajes.viaje'
    _description = "Viajes"

    titulo = fields.Char(required=True)
    fecha_inicio = fields.Date(default=fields.Date.today)
    duracion = fields.Float(digits=(6, 2), help="Duracion en días")
    plazas = fields.Integer(string="Numero de plazas disponibles")

    # En la relación many2one me permite elegir un partner/cliente o crear uno directamente
    # Tener en cuenta que solo aparecerán los partners/clientes que sean de tipo conductor
    conductor_id = fields.Many2one('res.partner', string="Conductor",
                                   domain=[('conductor', '=', True),
                                           ('category_id.name', 'ilike', "Conductor")])

    # En la relación many2one me permite elegir un vehiculo o crear uno directamente
    vehiculo_id = fields.Many2one('viajes.vehiculo',
                                  ondelete='cascade', string="Vehiculo", required=True)

    # puedo elegir uno(partner/cliente) que ya existe o crear uno nuevo
    pasajeros_ids = fields.Many2many('res.partner', string="Pasajeros")
