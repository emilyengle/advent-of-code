import math


# Part 1
def get_fuel_requirement(mass):
    fuel = math.floor(mass / 3) - 2
    return fuel if fuel > 0 else 0


# Part 2
def get_total_fuel_requirement(mass):
    fuel = get_fuel_requirement(mass)
    if fuel is 0:
        return 0

    return fuel + get_total_fuel_requirement(fuel)


def main():
    file = open('input.txt', 'r')

    total_fuel_req = 0
    for mass in file.readlines():
        m = int(mass)
        total_fuel_req += get_total_fuel_requirement(m)

    print(f'Total fuel required: {total_fuel_req}')


main()
