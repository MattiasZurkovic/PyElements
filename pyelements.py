__author__ = 'mattias'

# The following code is for the Python library/module called ElementsPy

#=======================================================================================================================


# IMPORTANT!: Each individual method for ech elements returns a LIST with all that elemnts DATA each element in that list has a different value! This is how the list's elements are formatted/arranged: [ELEMENT NAME, SYMBOL, ATOMIC #, ATOMIC MASS, EARTH STATE, FAMILY, NONMETAL/METAL] ---- (I.E. Helium => ['Helium', 'He', 2, 4, 'Gas', 'Noble Gases, 'Non-Metal']  *-*)

# This method had the user type the elements name and then they will retrieve the information about that element
def find_by_name(element_name):
    # Period 1
    if element_name == 'Hydrogen':
       return hydrogen_info()
    if element_name == 'Helium':
        return helium_info()
    # Period 2
    if element_name == 'Lithium':
        return lithium_info()
    if element_name == 'Beryllium':
        return beryllium_info()
    if element_name == 'Boron':
        return boron_info()
    if element_name == 'Carbon':
        return carbon_info()
    if element_name == 'Nitrogen':
        return nitrogen_info()
    if element_name == 'Oxygen':
        return oxygen_info()
    if element_name == 'Fluorine':
        return fluorine_info()
    if element_name == 'Neon':
        return neon_info()
    # Period 3
    if element_name == 'Sodium':
        return sodium_info()
    if element_name == 'Magnesium':
        return magnesium_info()
    if element_name == 'Aluminium':
        return aluminium_info()
    if element_name == 'Silicon':
        return silicon_info()
    if element_name == 'Phosphorus':
        return phosphorus_info()
    if element_name == 'Sulfur':
        return sulfur_info()
    if element_name == 'Chlorine':
        return chlorine_info()
    if element_name == 'Argon':
        return argon_info()


# This method had the user type the elements symbol (I.E. He) and then they will retrieve the information about that element

def find_by_symbol(symbol):
    return 'n0thing here... ...yet'

#-----------------------------------------------------------------------------------------------------------------------


# Below are the procedures for having all the information about each elements. They are ordered from least atomic number to greatest.

# Period 1
def hydrogen_info():
    name = 'Hydrogen'
    symbol = 'H'
    atomic_number = 1
    atomic_mass = 1.008
    earth_state = 'Gas'
    family = ''
    metal_nonmetal = 'Non-Metal'
    # return ('Name: ' + name + ' |', 'Symbol: ' + symbol + ' |', 'Atomic Number: ' + atomic_number + ' |', 'Atomic Mass: ' + atomic_mass + ' |', 'Earth State: ' + earth_state + ' |', 'Family: ' + family + ' |', 'Metal/Non-Metal: ' + metal_nonmetal)
    info_list = [name, symbol, atomic_number, atomic_mass, earth_state, family, metal_nonmetal]
    return info_list

def helium_info():
    name = 'Helium'
    symbol = 'He'
    atomic_number = 2
    atomic_mass = 4
    earth_state = 'Gas'
    family = 'Noble Gases'
    metal_nonmetal = 'Non-Metal'
    info_list = [name, symbol, atomic_number, atomic_mass, earth_state, family, metal_nonmetal]
    return info_list

# Period 2
def lithium_info():
    name = 'Lithium'
    symbol = 'Li'
    atomic_number = 3
    atomic_mass = 6.94
    earth_state = 'Solid'
    family = 'Alkali Metals'
    metal_nonmetal = 'Metal'
    info_list = [name, symbol, atomic_number, atomic_mass, earth_state, family, metal_nonmetal]
    return info_list

def beryllium_info():
    name = 'Beryllium'
    symbol = 'Be'
    atomic_number = 4
    atomic_mass = 9.0121
    earth_state = 'Solid'
    family = 'Alkali Earth Metals'
    metal_nonmetal = 'Metal'
    info_list = [name, symbol, atomic_number, atomic_mass, earth_state, family, metal_nonmetal]
    return info_list

def boron_info():
    name = 'Boron'
    symbol = 'B'
    atomic_number = 5
    atomic_mass = 10.81
    earth_state = 'Solid'
    family = 'Group 13'
    metal_nonmetal = 'Metalloid'
    info_list = [name, symbol, atomic_number, atomic_mass, earth_state, family, metal_nonmetal]
    return info_list

def carbon_info():
    name = 'Carbon'
    symbol = 'C'
    atomic_number = 6
    atomic_mass = 12.011
    earth_state = 'Solid'
    family = 'Group 14'
    metal_nonmetal = 'Non-Metal'
    info_list = [name, symbol, atomic_number, atomic_mass, earth_state, family, metal_nonmetal]
    return info_list

def nitrogen_info():
    name = 'Nitrogen'
    symbol = 'N'
    atomic_number = 7
    atomic_mass = 14.007
    earth_state = 'Gas'
    family = 'Group 15'
    metal_nonmetal = 'Non-Metal'
    info_list = [name, symbol, atomic_number, atomic_mass, earth_state, family, metal_nonmetal]
    return info_list

def oxygen_info():
    name = 'Oxygen'
    symbol = 'O'
    atomic_number = 8
    atomic_mass = 15.999
    earth_state = 'Gas'
    family = 'Group 16'
    metal_nonmetal = 'Non-Metal'
    info_list = [name, symbol, atomic_number, atomic_mass, earth_state, family, metal_nonmetal]
    return info_list

def fluorine_info():
    name = 'Fluorine'
    symbol = 'F'
    atomic_number = 9
    atomic_mass = 18.998
    earth_state = 'Gas'
    family = 'Halogens'
    metal_nonmetal = 'Non-Metal'
    info_list = [name, symbol, atomic_number, atomic_mass, earth_state, family, metal_nonmetal]
    return info_list

def neon_info():
    name = 'Neon'
    symbol = 'Ne'
    atomic_number = '10'
    atomic_mass = '20.1797'
    earth_state = 'Gas'
    family = 'Noble Gases'
    metal_nonmetal = 'Non-Metal'
    info_list = [name, symbol, atomic_number, atomic_mass, earth_state, family, metal_nonmetal]
    return info_list

# Period 3
def sodium_info():
    name = 'Sodium'
    symbol = 'Na'
    atomic_number = 11
    atomic_mass = 29.989
    earth_state = 'Solid'
    family = 'Alkali Metals'
    metal_nonmetal = 'Metal'
    info_list = [name, symbol, atomic_number, atomic_mass, earth_state, family, metal_nonmetal]
    return info_list

def magnesium_info():
    name = 'Magnesium'
    symbol = 'Mg'
    atomic_number = 12
    atomic_mass = 24.305
    earth_state = 'Solid'
    family = 'Alkaline Earth Metals'
    metal_nonmetal = 'Metal'
    info_list = [name, symbol, atomic_number, atomic_mass, earth_state, family, metal_nonmetal]
    return info_list

def aluminium_info():
    name = 'Aluminium'
    symbol = 'Al'
    atomic_number = 13
    atomic_mass = 26.981
    earth_state = 'Solid'
    family = 'Post-transition metals'
    metal_nonmetal = 'Metal'
    info_list = [name, symbol, atomic_number, atomic_mass, earth_state, family, metal_nonmetal]
    return info_list

def silicon_info():
    name = 'Silicon'
    symbol = 'Si'
    atomic_number = 14
    atomic_mass = 20.085
    earth_state = 'Solid'
    family = 'Group 14'
    metal_nonmetal = 'Metalliod'
    info_list = [name, symbol, atomic_number, atomic_mass, earth_state, family, metal_nonmetal]
    return info_list

def phosphorus_info():
    name = 'Phosphorus'
    symbol = 'P'
    atomic_number = 15
    atomic_mass = 20.973
    earth_state = 'Solid'
    family = 'Group 15'
    metal_nonmetal = 'Non-Metal'
    info_list = [name, symbol, atomic_number, atomic_mass, earth_state, family, metal_nonmetal]
    return info_list

def sulfur_info():
    name = 'Sulfur'
    symbol = 'S'
    atomic_number = 16
    atomic_mass = 32.06
    earth_state = 'Solid'
    family = 'Group 16'
    metal_nonmetal = 'Non-Metal'
    info_list = [name, symbol, atomic_number, atomic_mass, earth_state, family, metal_nonmetal]
    return info_list

def chlorine_info():
    name = 'Chlorine'
    symbol = 'Cl'
    atomic_number = 17
    atomic_mass = 35.35
    earth_state = 'Gas'
    family = 'Halogens'
    metal_nonmetal = 'Non-Metal'
    info_list = [name, symbol, atomic_number, atomic_mass, earth_state, family, metal_nonmetal]
    return info_list

def argon_info():
    name = 'Argon'
    symbol = 'Ar'
    atomic_number = 18
    atomic_mass = 39.984
    earth_state = 'Gas'
    family = 'Noble Gases'
    metal_nonmetal = 'Non-Metal'
    info_list = [name, symbol, atomic_number, atomic_mass, earth_state, family, metal_nonmetal]
    return info_list

# Period 4
def potassium_info():
    name = 'Potassium'
    symbol = 'K'
    atomic_number = 19
    atomic_mass = 39.0983
    earth_state = 'Solid'
    family = 'Alkali Metals'
    metal_nonmetal = 'Metal'
    info_list = [name, symbol, atomic_number, atomic_mass, earth_state, family, metal_nonmetal]
    return info_list