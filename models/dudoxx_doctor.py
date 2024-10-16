from odoo import models, fields, api

class DudoxxDoctor(models.Model):
    _name = 'dudoxx.doctor'
    _description = 'Doctor Profile'

    name = fields.Char(string='Full Name', required=True)
    specialty = fields.Char(string='Specialty')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone Number')
    license_number = fields.Char(string='Medical License Number')
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('retired', 'Retired')
    ], string='Status', default='active')
    experience_years = fields.Integer(string='Years of Experience')
    photo = fields.Binary(string='Profile Photo')

    @api.depends('name', 'license_number')
    def name_get(self):
        result = []
        for doctor in self:
            name = f"{doctor.name} ({doctor.license_number})" if doctor.license_number else doctor.name
            result.append((doctor.id, name))
        return result

    def activate(self):
        self.write({'status': 'active'})

    def deactivate(self):
        self.write({'status': 'inactive'})

    def retire(self):
        self.write({'status': 'retired'})