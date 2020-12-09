import re

def get_passport_list():
    passports = []
    file = open('input.txt', 'r')
    
    pp = {}
    for line in file.readlines():
        if line == '\n':
            passports.append(pp)
            pp = {}
        else:
            fields = line.strip('\n').split(' ')
            for field in fields:
                [key, value] = field.split(':')
                pp[key] = value
    passports.append(pp)

    return passports


def has_required_fields(passport):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return len([r for r in required if r in passport]) == len(required)


def has_valid_birthyear(passport):
    byr = int(passport['byr'])
    return byr >= 1920 and byr <= 2002


def has_valid_issueyear(passport):
    iyr = int(passport['iyr'])
    return iyr >= 2010 and iyr <= 2020


def has_valid_expyear(passport):
    eyr = int(passport['eyr'])
    return eyr >= 2020 and eyr <= 2030


def has_valid_height(passport):
    height = passport['hgt']
    if not re.match('^[0-9]{2,3}(cm|in)$', height):
        return False
    height_num = int(height[0:len(height)-2])
    height_suffix = height[len(height)-2:len(height)]
    if height_suffix == 'cm':
        return height_num >= 150 and height_num <= 193
    return height_num >= 59 and height_num <= 76


def has_valid_haircolor(passport):
    hcl = passport['hcl']
    return re.match('^#[\w\d]{6}$', hcl)


def has_valid_eyecolor(passport):
    ecl = passport['ecl']
    valid_ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return ecl in valid_ecls


def has_valid_pid(passport):
    pid = passport['pid']
    return len(pid) == 9 and re.match('^[0-9]*$', pid)


def has_valid_fields(passport):
    return has_valid_birthyear(passport) and has_valid_issueyear(passport) and has_valid_expyear(passport) and has_valid_eyecolor(passport) and has_valid_pid(passport) and has_valid_haircolor(passport) and has_valid_height(passport)


if __name__ == '__main__':
    passports = get_passport_list()

    num_valid = 0
    for passport in passports:
        if (has_required_fields(passport) and has_valid_fields(passport)):
            num_valid += 1
    print(num_valid)