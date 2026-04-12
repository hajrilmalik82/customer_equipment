from odoo import models, fields

class EquipmentService(models.Model):
    _name = 'equipment.service'
    _description = 'Equipment Service History'

    equipment_id = fields.Many2one('customer.equipment', string='Equipment', required=True, ondelete='cascade')
    
    service_date = fields.Date(string='Tanggal Service', default=fields.Date.context_today)
    description = fields.Text(string='Deskripsi')
    cost = fields.Float(string='Biaya')
    technician = fields.Char(string='Nama Teknisi')
    #test