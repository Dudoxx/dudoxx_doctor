from odoo import models, fields, api
from datetime import datetime, timedelta
import secrets
import string

class DudoxxApiKey(models.Model):
    _name = 'dudoxx.api.key'
    _description = 'API Key'

    key = fields.Char(string='API Key', required=True, readonly=True)
    service_name = fields.Char(string='Service Name', required=True)
    doctor_id = fields.Many2one('dudoxx.doctor', string='Doctor', required=True)
    created_date = fields.Datetime(string='Created Date', default=fields.Datetime.now, readonly=True)
    expiry_date = fields.Datetime(string='Expiry Date', required=True)
    status = fields.Selection([
        ('active', 'Active'),
        ('revoked', 'Revoked'),
        ('expired', 'Expired')
    ], string='Status', default='active', compute='_compute_status', store=True)

    @api.depends('expiry_date')
    def _compute_status(self):
        now = fields.Datetime.now()
        for record in self:
            if record.status == 'revoked':
                continue
            if record.expiry_date and record.expiry_date < now:
                record.status = 'expired'
            else:
                record.status = 'active'

    @api.model
    def create(self, vals):
        if 'key' not in vals:
            vals['key'] = self.generate_api_key()
        if 'expiry_date' not in vals:
            vals['expiry_date'] = fields.Datetime.now() + timedelta(days=365)
        return super(DudoxxApiKey, self).create(vals)

    def revoke_key(self):
        self.write({'status': 'revoked'})

    def regenerate_key(self):
        self.write({
            'key': self.generate_api_key(),
            'created_date': fields.Datetime.now(),
            'expiry_date': fields.Datetime.now() + timedelta(days=365),
            'status': 'active'
        })

    @api.model
    def generate_api_key(self):
        """Generate a new API key."""
        alphabet = string.ascii_letters + string.digits
        api_key = ''.join(secrets.choice(alphabet) for _ in range(32))
        return api_key

    def validate_key(self):
        """Validate the API key status and check expiry."""
        self.ensure_one()
        now = fields.Datetime.now()
        if self.status == 'revoked':
            return False, 'API key has been revoked'
        if self.expiry_date < now:
            self.status = 'expired'
            return False, 'API key has expired'
        return True, 'API key is valid'