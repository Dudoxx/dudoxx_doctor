from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta

class TestApiKey(TransactionCase):

    def setUp(self):
        super(TestApiKey, self).setUp()
        self.api_key_model = self.env['dudoxx.api.key']
        self.doctor_model = self.env['dudoxx.doctor']
        self.doctor = self.doctor_model.create({
            'name': 'Dr. Test Doctor',
            'license_number': 'TEST123'
        I apologize for the confusion. It seems the message was cut off while creating the test file for the API key model. Let's complete that file and continue with the task.

<write_to_file>
<path>dudoxx_doctor/tests/test_api_key.py</path>
<content>
from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta

class TestApiKey(TransactionCase):

    def setUp(self):
        super(TestApiKey, self).setUp()
        self.api_key_model = self.env['dudoxx.api.key']
        self.doctor_model = self.env['dudoxx.doctor']
        self.doctor = self.doctor_model.create({
            'name': 'Dr. Test Doctor',
            'license_number': 'TEST123'
        })

    def test_create_api_key(self):
        api_key = self.api_key_model.create({
            'service_name': 'Test Service',
            'doctor_id': self.doctor.id,
        })
        self.assertTrue(api_key.key)
        self.assertEqual(api_key.status, 'active')
        self.assertTrue(api_key.expiry_date)

    def test_generate_api_key(self):
        key = self.api_key_model.generate_api_key()
        self.assertEqual(len(key), 32)
        self.assertTrue(key.isalnum())

    def test_validate_key(self):
        api_key = self.api_key_model.create({
            'service_name': 'Test Service',
            'doctor_id': self.doctor.id,
        })
        
        # Test valid key
        valid, message = api_key.validate_key()
        self.assertTrue(valid)
        self.assertEqual(message, 'API key is valid')

        # Test expired key
        api_key.expiry_date = datetime.now() - timedelta(days=1)
        valid, message = api_key.validate_key()
        self.assertFalse(valid)
        self.assertEqual(message, 'API key has expired')
        self.assertEqual(api_key.status, 'expired')

        # Test revoked key
        api_key.revoke_key()
        valid, message = api_key.validate_key()
        self.assertFalse(valid)
        self.assertEqual(message, 'API key has been revoked')

    def test_regenerate_key(self):
        api_key = self.api_key_model.create({
            'service_name': 'Test Service',
            'doctor_id': self.doctor.id,
        })
        old_key = api_key.key
        old_expiry = api_key.expiry_date

        api_key.regenerate_key()
        self.assertNotEqual(api_key.key, old_key)
        self.assertNotEqual(api_key.expiry_date, old_expiry)
        self.assertEqual(api_key.status, 'active')