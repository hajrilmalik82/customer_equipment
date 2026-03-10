from odoo import models, fields, api, _
from datetime import date

class CustomerEquipment(models.Model):
    _name = 'customer.equipment'
    _description = 'Customer Equipment'

    name = fields.Char(string='Nama Equipment', required=True)
    serial_number = fields.Char(string='Serial Number', required=True)
    customer_id = fields.Many2one('res.partner', string='Pemilik', required=True)
    purchase_date = fields.Date(string='Tanggal Beli')
    warranty_expired = fields.Date(string='Garansi Habis')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('retired', 'Retired')
    ], string='Status', default='draft')
    service_ids = fields.One2many('equipment.service', 'equipment_id', string='Riwayat Service')

    total_cost = fields.Float(string='Total Biaya Service', compute='_compute_total_cost', store=True)


    _sql_constraints = [
        ('serial_number_unique', 'unique(serial_number)', 'Serial number tidak boleh duplikat!')
    ]

    @api.depends('service_ids.cost')
    def _compute_total_cost(self):
        for record in self:
            record.total_cost = sum(record.service_ids.mapped('cost'))

    @api.onchange('warranty_expired')
    def _onchange_warranty_expired(self):
        if self.warranty_expired and self.warranty_expired < date.today():
            return {
                'warning': {
                    'title': _('Peringatan Garansi'),
                    'message': _('Masa garansi untuk equipment ini sudah habis!'),
                }
            }