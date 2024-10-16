# Dudoxx Doctor

## Overview

Dudoxx Doctor is an Odoo 16 module designed to manage doctor profiles and handle API keys for various cloud services. This module provides features for managing doctor information, API key lifecycle, security roles, and access controls.

## Features

- Doctor profile management
  - Create and manage doctor profiles with detailed information
  - Track doctor status (Active, Inactive, Retired)
  - Manage doctor specialties and experience
- API key generation and management
  - Generate secure API keys for doctors
  - Manage API key lifecycle (creation, expiration, revocation)
  - Validate API keys
- Role-based access control
  - Define different access levels for administrators, doctors, and API key managers
- User-friendly views for doctor profiles and API keys
- Custom widgets for displaying status information

## Installation

1. Ensure you have Odoo 16 installed and running.
2. Clone this repository into your Odoo addons directory:
   ```
   git clone https://github.com/Dudoxx/dudoxx_doctor.git
   ```
3. Update your Odoo addons list:
   - Go to Apps menu
   - Click on "Update Apps List"
4. Search for "Dudoxx Doctor" in the Apps menu and click Install.

## Configuration

After installation, you can configure the module by following these steps:

1. Go to Settings > Users & Companies > Users
2. Select the user you want to grant access to
3. Under "Access Rights" tab, you can assign one of the following roles:
   - Doctor Admin: Full control over doctor profiles and API keys
   - Doctor User: Limited access to view and edit their own profile
   - API Key Manager: Manage API keys for all doctors

## Usage

### Managing Doctor Profiles

1. Go to Dudoxx Doctor > Doctors
2. Click "Create" to add a new doctor profile
3. Fill in the required information:
   - Name
   - Specialty
   - License Number
   - Contact Information
4. You can change the doctor's status using the buttons at the top of the form:
   - Activate
   - Deactivate
   - Retire

### Managing API Keys

1. Go to Dudoxx Doctor > API Keys
2. Click "Create" to generate a new API key
3. Select the doctor and service name for the API key
4. The key will be automatically generated
5. You can revoke or regenerate the key using the buttons at the top of the form

## Troubleshooting

1. **Issue**: Cannot see the Dudoxx Doctor menu
   **Solution**: Ensure that the user has the correct access rights assigned (Doctor Admin, Doctor User, or API Key Manager)

2. **Issue**: API key validation fails
   **Solution**: Check the following:
   - Ensure the API key has not expired
   - Verify that the API key has not been revoked
   - Confirm that the doctor associated with the API key is still active

3. **Issue**: Cannot create or edit doctor profiles
   **Solution**: Verify that the user has Doctor Admin rights. Doctor Users can only edit their own profiles.

## Support

For support, please contact Dudoxx UG at support@dudoxx.com or create an issue in the GitHub repository.

## Contributing

We welcome contributions to the Dudoxx Doctor module. Please read our contributing guidelines before submitting pull requests.

## License

This module is licensed under the LGPL-3. See the LICENSE file for full details.