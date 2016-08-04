import urllib2
import json

element_json = "https://gist.githubusercontent.com/peterellisjones/758549cd18d4665163d8774e6bea6f6b/raw/a3f2b8abb87c8baabd099f658483b5617e9c3f59/Periodic%2520Table%2520Elements%2520JSON%2520Format"
response = urllib2.urlopen(element_json)
parsed_data = json.loads(response.read())

element_names = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Ununnilium", "Unununium", "Ununbium", "Ununtrium", "Ununquadium", "Ununpentium", "Ununhexium", "Ununseptium", "Ununoctium"]

json_keys = ["atomic_number", "abbreviation", "atomic_weight"]

def format_info(target):
	elem_values = []
        target_json = parsed_data[target]
        for i in json_keys:
                elem_values.append(target_json[i])
	return elem_values
	

def get_by_name(elem_name):
	return format_info(elem_name.upper())

def get_by_atomic_number(atomic_number):
	element_ans = element_names[atomic_number - 1]
	return format_info(element_ans.upper()) 
 
print get_by_name("Thorium")
print get_by_atomic_number(4)

print parsed_data['HYDROGEN']['atomic_number']
