from balance_equation import balance_equation

elements = {
    'H': 1.008,
    'He': 4.003,
    'Li': 6.941,
    'Be': 9.012,
    'B': 10.81,
    'C': 12.011,
    'N': 14.007,
    'O': 15.999,
    'F': 18.998,
    'Ne': 20.18,
    'Na': 22.990,
    'Mg': 24.305,
    'Al': 26.982,
    'Si': 28.086,
    'P': 30.974,
    'S': 32.066,
    'Cl': 35.453,
    'Ar': 39.948,
    'K': 39.098,
    'Ca': 40.078,
    'Sc': 44.956,
    'Ti': 47.867,
    'Cr': 51.996,
    'Mn': 54.938,
    'Fe': 55.845,
    'Co': 58.933,
    'Ni': 58.693,
    'Cu': 63.546,
    'Zn': 65.38,
    'Ga': 69.723,
    'Ge': 72.631,
    'As': 74.922,
    'Se': 78.971,
    'Br': 79.904,
    'Kr': 83.798,
    'Rb': 85.468,
    'Sr': 87.62,
    'Y': 88.906,
    'Zr': 91.224,
    'Nb': 92.906,
    'Mo': 95.95,
    'Tc': 98.907,
    'Ru': 101.07,
    'Rh': 102.906,
    'Pd': 106.42,
    'Ag': 107.868,
    'Cd': 112.414,
    'In': 114.818,
    'Sn': 118.711,
    'Sb': 121.760,
    'Te': 127.6,
    'I': 126.904,
    'Xe': 131.293,
    'Cs': 132.905,
    'Ba': 137.328,
    'La': 138.905,
    'Ce': 140.116,
    'Pr': 140.908,
    'Nd': 144.243,
    'Pm': 144.913,
    'Sm': 150.36,
    'Eu': 151.964,
    'Gd': 157.25,
}

# Balancing Chemical Equations

def dissolve(compound):
    slice_point = 0
    multiplied_compound = []
    end_paren = 0
    for i in range(0, len(compound)):
        letter = compound[i]
        inside_compound = ''
        if letter == '(':
            slice_point = i + 1
        elif letter == ')':
            inside_compound = compound[slice_point:i]
            end_paren = i
            multiplied_compound = multiply(inside_compound,compound[i+1])
    return compound[:slice_point-1] + ' '.join(multiplied_compound) +  compound[end_paren+2:]

def multiply(compound, multiplier):
    elements = compound.split()
    multiplied = []
    for element in elements:
        try:
            if ord(element[-2]) < 58:
                # Do some shit
                # TODO
                pass
        except:
            pass
        if ord(element[-1]) < 58:
            new_multiplier = int(element[-1]) * int(multiplier)
            mult_list = list(element)
            mult_list[-1] = str(new_multiplier)
            element = ''.join(mult_list)
            multiplied.append(element)
        else:
            element += multiplier
            multiplied.append(element)
    return multiplied



# Separating Elements into Dictionary
def seperate_element(compound_str):
    compound = list(compound_str)
    elements_list = []
    current_element = ''
    element = ''
    for letter in range(0, len(compound)):
        if compound[letter].isupper():
            current_element = compound[letter]
            print(current_element)
            try: 
                if compound[letter + 1].isupper():
                    element = current_element
            except:
                element = current_element
        else:
            current_element = current_element + compound[letter]
            element = current_element
        try:
            if ord(compound[letter + 1]) < 58:
                
                elements_list += [element]
            else:
                elements_list += [element]
        except:
            elements_list += [element]

    print(elements_list)
    return elements_list

def get_weight(compound):
    compound_weight = 0
    for element in compound:
        if ord(element[-1]) < 58:
            element_mass = elements[element[:-1]]
            element_quantity = int(element[-1])
            compound_weight += element_mass * element_quantity
        else:
            compound_weight += elements[element]
    return compound_weight

# Calculate Wanted Mass
def calc_mass(quantity, compound_one_weight, bal_one, compound_two_weight, bal_two):
    return (quantity*bal_two*compound_two_weight)/(compound_one_weight*bal_one)

def calc_stoich(given_compound, given_const, given_weight, wanted_compound, wanted_const):
    given_elements = given_compound.split()
    given_mass = get_weight(given_elements)

    wanted_elements = wanted_compound.split()
    wanted_mass = get_weight(wanted_elements)

    wanted_weight = calc_mass(given_weight, given_mass, given_const, wanted_mass, wanted_const)

    return wanted_weight
    

def get_compounds_old():    
    # Ask for elements
    print("Enter the given compound:")
    compound_one = input()
    # compound_one = dissolve(compound_one_paren)
    compound_one_elements = compound_one.split()
    compound_one_weight = get_weight(compound_one_elements)


    print(compound_one_weight)
    '''
    for element in compound_one_elements:
        print(f"Enter the amount of {element}:")
        atom_quant = int(input())
        compound_one_weight += atom_quant * elements[element]
    '''

    print(f"Enter the amount of {compound_one} needed to balance the equation:")
    bal_one = int(input())

    print(f"Enter the given amount of {compound_one}(in grams):")
    quantity = float(input())

    print("Enter the wanted compound:")
    compound_two = input()
    compound_two_elements = compound_two.split()
    compound_two_weight = get_weight(compound_two_elements)


    print(f"Enter the amount of {compound_two} needed to balance the equation:")
    bal_two = int(input())


    print(f"{quantity}g of {compound_one} results in {calc_mass(quantity, compound_one_weight, bal_one, compound_two_weight, bal_two)}g of {compound_two}")

def get_compounds_experimental():
    print("Enter the compounds on the left side of the equation(seperated by a \"+\"):")
    side_one_raw = input()
    side_one = side_one_raw.split("+")

    print("Enter the compounds on the right side of the equation(seperated by a \"+\"):")
    side_two_raw = input()
    side_two = side_two_raw.split("+")

    balance_vals = balance_equation(side_one, side_two)
    left_vals = balance_vals[0]
    right_vals = balance_vals[1]

    print("Enter the given element:")
    given = input()

    if given in side_one:
        given_index = side_one.index(given)
        given_const = left_vals[given_index]
    elif given in side_two:
        given_index = side_two.index(given)
        given_const = right_vals[given_index]

    print(f"Enter the amount of {given} (in grams):")
    given_weight = input()

    print(f"{given_weight}g of {given} in the equation {side_one_raw} --> {side_two_raw} means the following mass will be used:")
    for i in range(0, len(side_one)):
        print(f"{calc_stoich(given, int(given_const), float(given_weight), side_one[i], int(left_vals[i]))}g of {side_one[i]}")

    for i in range(0, len(side_two)):
        print(f"{calc_stoich(given, int(given_const), float(given_weight), side_two[i], int(right_vals[i]))}g of {side_two[i]}")

get_compounds_old()