# ============================================

# Python Basics - Medical Records Validator

# FreeCodeCamp Python Course

# Author: Om Patel

# ============================================

import re

# Sample medical records data

medical_records = [

    {

        'patient_id': 'P1001',

        'age': 34,

        'gender': 'Female',

        'diagnosis': 'Hypertension',

        'medications': ['Lisinopril'],

        'last_visit_id': 'V2301',

    },

    {

        'patient_id': 'p1002',

        'age': 47,

        'gender': 'male',

        'diagnosis': 'Type 2 Diabetes',

        'medications': ['Metformin', 'Insulin'],

        'last_visit_id': 'v2302',

    },

    {

        'patient_id': 'P1003',

        'age': 29,

        'gender': 'female',

        'diagnosis': 'Asthma',

        'medications': ['Albuterol'],

        'last_visit_id': 'v2303',

    },

    {

        'patient_id': 'p1004',

        'age': 56,

        'gender': 'Male',

        'diagnosis': 'Chronic Back Pain',

        'medications': ['Ibuprofen', 'Physical Therapy'],

        'last_visit_id': 'V2304',

    }

]

def find_invalid_records(

    patient_id, age, gender, diagnosis, medications, last_visit_id

):

    """

    Validates each field of a patient record.

    Returns list of invalid field names.

    """

    constraints = {

        # Patient ID must match pattern P/p followed by digits

        'patient_id': isinstance(patient_id, str)

        and re.fullmatch('p\d+', patient_id, re.IGNORECASE),

        # Age must be integer and at least 18

        'age': isinstance(age, int) and age >= 18,

        # Gender must be male or female

        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),

        # Diagnosis must be string or None

        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,

        # Medications must be list of strings

        'medications': isinstance(medications, list)

        and all([isinstance(i, str) for i in medications]),

        # Visit ID must match pattern V/v followed by digits

        'last_visit_id': isinstance(last_visit_id, str)

        and re.fullmatch('v\d+', last_visit_id, re.IGNORECASE)

    }

    return [key for key, value in constraints.items() if not value]

def validate(data):

    """

    Validates entire medical records dataset.

    Checks format, structure and field values.

    """

    # Must be a list or tuple

    is_sequence = isinstance(data, (list, tuple))

    if not is_sequence:

        print('Invalid format: expected a list or tuple.')

        return False

    is_invalid = False

    key_set = set(

        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']

    )

    for index, dictionary in enumerate(data):

        # Each item must be a dictionary

        if not isinstance(dictionary, dict):

            print(f'Invalid format: expected a dictionary at position {index}.')

            is_invalid = True

            continue

        # Must have exact required keys

        if set(dictionary.keys()) != key_set:

            print(

                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'

            )

            is_invalid = True

            continue

        # Validate individual fields

        invalid_records = find_invalid_records(**dictionary)

        for key in invalid_records:

            val = dictionary[key]

            print(f"Unexpected format '{key}: {val}' at position {index}.")

            is_invalid = True

    if is_invalid:

        return False

    print('Valid format.')

    return True

# Run validation

validate(medical_records)
