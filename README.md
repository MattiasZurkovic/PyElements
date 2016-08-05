# PyElements

## About
PyElements is a Python library/module that allows for access of various information on the periodic table. For example, you can retrive a given elemnts atomic number, mass, melting point and other charactaristics.

## Methods
As of now, PyElements ships with several usable methods. They are listed below:
* `.get_by_name(element_name)` - This method retrives a given elements information by passing it name. The `element_name` is the parameter for the name of the desired element, for example "Hydrogen".
* `.get_by_atomic_number(atomic_number)` - Gets the information of the element by atomic number. The `atomic_number` parameter is the atomic number of the desired element.
* `.table_info(method)` - This method will display a given elements information in a neater way, instead of a list. the `method` parameter defines that you must pass a previous method that returns a list of an elements properties. For example you may pass `get_by_name("Helium")` and the method will print its information.

## Usage
### The `.get_by_name()` Method:
```
print pyelements.get_by_name("Thorium")
>>> [90, u'Th', 232.12]
```
### The `.get_by_atomic_number()` Method:
```
print pyelements.get_by_atomic_number(90)
>>> [90, u'Th', 232.12]
```

### The `.table_info()` Method:
```
pyelements.table_info(pyelements.get_by_name("Beryllium"))
>>> | Name          | Beryllium
>>> | Symbol        | Be
>>> | Atomic Number | 4
>>> | Atomic Mass   | 9.012
```

### The `.get_by_symbol` Method:
TODO
