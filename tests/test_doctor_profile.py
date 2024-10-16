from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestDoctorProfile(TransactionCase):

    def setUp(self):
        super(TestDoctorProfile, self).setUp()
        self.doctor_model = self.env['dudoxx.doctor']

    def test_create_doctor(self):
        doctor = self.doctor_model.create({
            'name': 'Dr. John Doe',
            'specialty': 'Cardiology',
            'license_number': 'MED12345',
            'email': 'john.doe@example.com',
            'phone': '1234567890',
            'experience_years': 10
        })
        self.assertEqual(doctor.name, 'Dr. John Doe')
        self.assertEqual(doctor.status, 'active')

    def test_name_get(self):
        doctor = self.doctor_model.create({
            'name': 'Dr. Jane Smith',
            'license_number': 'MED54321'
        })
        name = doctor.name_get()[0][1]
        self.assertEqual(name, 'Dr. Jane Smith (MED54321)')

    def test_status_transitions(self):
        doctor = self.doctor_model.create({
            'name': 'Dr. Bob Johnson',
            'status': 'active'
        })
        
        doctor.deactivate()
        self.assertEqual(doctor.status, 'inactive')
        
        doctor.activate()
        self.assertEqual(doctor.status, 'active')
        
        doctor.retire()
        self.assertEqual(doctor.status, 'retired')

    def test_experience_years_constraint(self):
        with self.assertRaises(ValidationError):
            self.doctor_model.create({
                'name': 'Dr. Invalid',
                'experience_years': -1
            })

    def test_email_constraint(self):
        with self.assertRaises(ValidationError):
            self.doctor_model.create({
                'name': 'Dr. Invalid Email',
                'email': 'invalid_email'
            })