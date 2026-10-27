from pyscript import document

non_metals = {
    'H': {
        'name': 'Hydrogen',
        'atomic_number': 1,
        'atomic_mass': 1.008
    },
    'He': {
        'name': 'Helium',
        'atomic_number': 2,
        'atomic_mass': 4.003
    },
    'C': {
        'name': 'Carbon',
        'atomic_number': 6,
        'atomic_mass': 12.011
    },
    'N': {
        'name': 'Nitrogen',
        'atomic_number': 7,
        'atomic_mass': 14.007
    },
    'O': {
        'name': 'Oxygen',
        'atomic_number': 8,
        'atomic_mass': 15.999
    },
    'F': {
        'name': 'Fluorine',
        'atomic_number': 9,
        'atomic_mass': 18.998
    },
    'Ne': {
        'name': 'Neon',
        'atomic_number': 10,
        'atomic_mass': 20.180
    },
    'P': {
        'name': 'Phosphorus',
        'atomic_number': 15,
        'atomic_mass': 30.974
    },
    'S': {
        'name': 'Sulfur',
        'atomic_number': 16,
        'atomic_mass': 32.06
    },
    'Cl': {
        'name': 'Chlorine',
        'atomic_number': 17,
        'atomic_mass': 35.45
    },
    'Ar': {
        'name': 'Argon',
        'atomic_number': 18,
        'atomic_mass': 39.948
    },
    'Se': {
        'name': 'Selenium',
        'atomic_number': 34,
        'atomic_mass': 78.971
    },
    'Br': {
        'name': 'Bromine',
        'atomic_number': 35,
        'atomic_mass': 79.904
    },
    'Kr': {
        'name': 'Krypton',
        'atomic_number': 36,
        'atomic_mass': 83.798
    },
    'I': {
        'name': 'Iodine',
        'atomic_number': 53,
        'atomic_mass': 126.904
    },
    'Xe': {
        'name': 'Xenon',
        'atomic_number': 54,
        'atomic_mass': 131.293
    },
    'Rn': {
        'name': 'Radon',
        'atomic_number': 86,
        'atomic_mass': 222
    }
} # dictionaries inside a dictionary

def search_details(event):
    symbol = document.getElementById("Element").value.strip() #gets user input (case sensitive)

    element = non_metals.get(symbol, {
        "name": "Element does not exist in the non-metals list. Make sure it is the element symbol with the proper cases.",
        "atomic_number": "-",
        "atomic_mass": "-"
    }) # if user input is not found in the non_metals list

    result = document.getElementById("result") #displays the result

    result.innerHTML = (
        f'<div class="element-symbol">{symbol}</div>'
        f'<div class="element-name">{element["name"]}</div>'
        f'<div class="element-info">'
        f'<span class="element-label">Atomic Number</span>'
        f'<span class="element-value">{element["atomic_number"]}</span>'
        f'</div>'
        f'<div class="element-info">'
        f'<span class="element-label">Atomic Mass</span>'
        f'<span class="element-value">{element["atomic_mass"]}</span>'
        f'</div>'
    ) #css style
