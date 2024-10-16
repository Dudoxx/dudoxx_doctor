# Task 2.1: Define Doctor Profile Model

## Objective
Create the main model to store doctor profile details.

## Steps Completed

1. Created `dudoxx_doctor.py` file in the `models` directory.
2. Defined the `dudoxx.doctor` model with the following fields:
   - `name` (Char): Doctor's full name, required
   - `specialty` (Char): Medical specialty
   - `email` (Char): Contact email
   - `phone` (Char): Contact phone number
   - `license_number` (Char): Medical license number
   - `status` (Selection): Active or inactive status
   - `experience_years` (Integer): Years of experience
   - `photo` (Binary): Profile photo of the doctor
3. Implemented a custom `name_get` method to display the doctor's name along with their license number.
4. Updated `models/__init__.py` to import the new model.

## File Contents

### models/dudoxx_doctor.py
```python
[Content of dudoxx_doctor.py file]
```

### models/__init__.py
```python
from . import dudoxx_doctor
```

## Result
The Doctor Profile Model (`dudoxx.doctor`) has been successfully created with all the specified fields. The model is now ready to be used for storing and managing doctor profile information.

## Next Steps
Proceed with Task 2.2: Define API Key Model.