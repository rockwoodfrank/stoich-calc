import random

side_one = {
}

side_two = {
}

def accumulate_dict(original_dict, new_dict):
    for val in new_dict:
        try:
            if original_dict[val]:
                original_dict[val] += new_dict[val]
        except:
            original_dict[val] = new_dict[val]

    return original_dict

# Adding elements to dictionaries
def add_to_dict(compound):
    compound_elements = compound.split()
    element_dict = {}
    add_to = ''
    quantity = 0
    for element in compound_elements:
        try:
            if ord(element[-2]) < 58:
                add_to = element[:-2]
                quantity = int(element[-2:])
                print(f'{add_to}: {quantity}')
        except:
            pass
        if ord(element[-1]) < 58:
            add_to = element[:-1]
            quantity = int(element[-1])
        else:
            add_to = element
            quantity = 1
        try:
            element_dict[add_to]
            print(f'{element_dict[add_to]} is already in the list.')
            element_dict[add_to] += quantity
        except:
            element_dict[add_to] = quantity
    return element_dict


def multiply_equation(compound_dict, multiplier):
    final_dict = {}
    for obj in compound_dict:
        final_dict[obj] = compound_dict[obj] * multiplier

    return final_dict

'''side_one = add_to_dict('H2 O2 S3 Cr H')
side_one.update(add_to_dict('Fe'))
side_one_mult = multiply_equation(side_one, 20)'''
def balance_equation(side_one_compounds, side_two_compounds):
    i = 1
    balanced = False
    side_one = {}
    while not balanced:
        side_one = {}
        side_two = {}
        side_one_constants = []
        side_two_constants = []
        for compound in side_one_compounds:
            ind_compound = add_to_dict(compound)
            random_balancer = random.randrange(1,10)
            side_one_constants += [random_balancer]
            ind_mult = multiply_equation(ind_compound, random_balancer)
            side_one = accumulate_dict(side_one, ind_mult)

        for compound in side_two_compounds:
            ind_compound = add_to_dict(compound)
            random_balancer = random.randint(1,10)
            side_two_constants += [random_balancer]
            ind_mult = multiply_equation(ind_compound, random_balancer)
            side_two = accumulate_dict(side_two, ind_mult)

        if side_one == side_two:
            balanced = True

    return [side_one_constants, side_two_constants]