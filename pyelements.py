#!/bin/env python
import urllib2
import json
from texttable import Texttable
from sys import stdout

element_json = "https://gist.githubusercontent.com/peterellisjones/758549cd18d4665163d8774e6bea6f6b/raw/a3f2b8abb87c8baabd099f658483b5617e9c3f59/Periodic%2520Table%2520Elements%2520JSON%2520Format"
response = urllib2.urlopen(element_json)
parsed_data = json.loads(response.read())

element_names = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Ununnilium", "Unununium", "Ununbium", "Ununtrium", "Ununquadium", "Ununpentium", "Ununhexium", "Ununseptium", "Ununoctium"]

json_keys = ["atomic_number", "abbreviation", "atomic_weight"]

def format_info(target):
	elem_values = []
        target_json = parsed_data[target]
        for i in json_keys:
                elem_values.append(target_json[i])
	return elem_values

def table_info(info):
	print "| Name          | " + element_names[info[0] - 1]
	print "| Symbol        | " + info[1]
	print "| Atomic Number | " + str(info[0])
	print "| Atomic Mass   | " + str(info[-1])	

# This method checks the spelling type of the element
def check_name(prov):
	if prov == "Aluminum":
		return "Aluminium"
	elif prov == "Sulfur":
		return "Sulphur"
	elif prov == "Cesium":
		return "Caesium"
	else:
		return True

def get_by_name(elem_name):
	elem_checked = check_name(elem_name)
	if elem_checked != True:
		return format_info(elem_checked.upper())
	else: # Default to...
		return format_info(elem_name.upper())

def get_by_atomic_number(atomic_number):
	element_ans = element_names[atomic_number - 1]
	if check_name(element_ans) != True:
		return format_info(check_name(element_ans).upper()) 
	else:
		return format_info(element_ans.upper())

print get_by_name("Cesium")


for i in range (1, 99):
	print table_info(get_by_atomic_number(i))
 
print get_by_name("Thorium")
table_info(get_by_atomic_number(4))
print get_by_atomic_number(1)


