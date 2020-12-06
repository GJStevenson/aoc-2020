import re

class Passport:
    def __init__(self):
        self._field_names = set()
        self._fields = {}

    def add_property(self, field):
        field_name, value = field.split(':')
        self._fields[field_name] = value
        self._field_names.add(field_name)

    def is_valid(self):
        hcl_pattern = re.compile("#[0-9a-f]")
        pid_pattern = re.compile("\d{9}$")

        byr_valid = 1920 <= int(self._fields.get('byr', 0)) <= 2002
        iyr_valid = 2010 <= int(self._fields.get('iyr', 0)) <= 2020
        eyr_valid = 2020 <= int(self._fields.get('eyr', 0)) <= 2030
        hcl_valid = hcl_pattern.match(self._fields.get('hcl', '')) is not None
        ecl_valid = self._fields.get('ecl', '') in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        pid_valid = pid_pattern.match(self._fields.get('pid', '')) is not None

        hgt_valid = False
        height = self._fields.get('hgt', '')
        if height.endswith('cm'):
            hgt_valid = 150 <= int(re.findall(r'\d+', height)[0]) <= 193
        if height.endswith('in'):
            hgt_valid = 59 <= int(re.findall(r'\d+', height)[0]) <= 76

        return byr_valid and iyr_valid and eyr_valid and hcl_valid and hcl_valid and ecl_valid and pid_valid and hgt_valid

    def contains_valid_fields(self):
        valid_passport_credentials = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])
        valid_north_pole_credentials = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

        return self._field_names == valid_north_pole_credentials or self._field_names == valid_passport_credentials
