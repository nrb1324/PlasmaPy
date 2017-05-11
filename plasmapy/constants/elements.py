"""Structures containing atomic data"""

from astropy import units as u, constants as const

atomic_symbols_list = ["n", "H", "He", "Li", "Be", "B", "C", "N", "O",
                       "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S",
                       "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr",
                       "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge",
                       "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
                       "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd",
                       "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba",
                       "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd",
                       "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf",
                       "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
                       "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra",
                       "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm",
                       "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf",
                       "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn",
                       "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]

atomic_symbols_dict = {"hydrogen": "H", "helium": "He", "lithium": "Li",
                       "beryllium": "Be", "boron": "B", "carbon": "C",
                       "nitrogen": "N", "oxygen": "O", "fluorine": "F",
                       "neon": "Ne", "sodium": "Na", "magnesium": "Mg",
                       "aluminium": "Al", "silicon": "Si", "phosphorus": "P",
                       "sulfur": "S", "chlorine": "Cl", "argon": "Ar",
                       "potassium": "K", "calcium": "Ca", "scandium": "Sc",
                       "titanium": "Ti", "vanadium": "V", "chromium": "Cr",
                       "manganese": "Mn", "iron": "Fe", "cobalt": "Co",
                       "nickel": "Ni", "copper": "Cu", "zinc": "Zn",
                       "gallium": "Ga", "germanium": "Ge", "arsenic": "As",
                       "selenium": "Se", "bromine": "Br", "krypton": "Kr",
                       "rubidium": "Rb", "strontium": "Sr", "yttrium": "Y",
                       "zirconium": "Zr", "niobium": "Nb", "molybdenum": "Mo",
                       "technetium": "Tc", "ruthenium": "Ru", "rhodium": "Rh",
                       "palladium": "Pd", "silver": "Ag", "cadmium": "Cd",
                       "indium": "In", "tin": "Sn", "antimony": "Sb",
                       "tellurium": "Te", "iodine": "I", "xenon": "Xe",
                       "caesium": "Cs", "barium": "Ba", "lanthanum": "La",
                       "cerium": "Ce", "praseodymium": "Pr", "neodymium": "Nd",
                       "promethium": "Pm", "samarium": "Sm", "europium": "Eu",
                       "gadolinium": "Gd", "terbium": "Tb", "dysprosium": "Dy",
                       "holmium": "Ho", "erbium": "Er", "thulium": "Tm",
                       "ytterbium": "Yb", "lutetium": "Lu", "hafnium": "Hf",
                       "tantalum": "Ta", "tungsten": "W", "rhenium": "Re",
                       "osmium": "Os", "iridium": "Ir", "platinum": "Pt",
                       "gold": "Au", "mercury": "Hg", "thallium": "Tl",
                       "lead": "Pb", "bismuth": "Bi", "polonium": "Po",
                       "astatine": "At", "radon": "Rn", "francium": "Fr",
                       "radium": "Ra", "actinium": "Ac", "thorium": "Th",
                       "protactinium": "Pa", "uranium": "U", "neptunium": "Np",
                       "plutonium": "Pu", "americium": "Am", "curium": "Cm",
                       "berkelium": "Bk", "californium": "Cf",
                       "einsteinium": "Es", "fermium": "Fm",
                       "mendelevium": "Md", "nobelium": "No",
                       "lawrencium": "Lr", "rutherfordium": "Rf",
                       "dubnium": "Db", "seaborgium": "Sg", "bohrium": "Bh",
                       "hassium": "Hs", "meitnerium": "Mt",
                       "darmstadtium": "Ds", "roentgenium": "Rg",
                       "copernicium": "Cn", "nihonium": "Nh",
                       "flerovium": "Fl", "moscovium": "Mc",
                       "livermorium": "Lv", "tennessine": "Ts",
                       "oganesson": "Og", "neutron": "n"}

Elements = {
    "n": {"atomic_number": 0, "symbol": "n",
          "name": "neutron"},
    "H": {"atomic_number": 1, "symbol": "H",
          "atomic_mass": 1.008*u.u, "name": "hydrogen"},
    "He": {"atomic_number": 2, "symbol": "He",
           "atomic_mass": 4.002602*u.u, "name": "helium"},
    "Li": {"atomic_number": 3, "symbol": "Li",
           "atomic_mass": 6.94*u.u, "name": "lithium"},
    "Be": {"atomic_number": 4, "symbol": "Be",
           "atomic_mass": 9.0121831*u.u, "name": "beryllium"},
    "B": {"atomic_number": 5, "symbol": "B",
          "atomic_mass": 10.806*u.u, "name": "boron"},
    "C": {"atomic_number": 6, "symbol": "C",
          "atomic_mass": 12.011*u.u, "name": "carbon"},
    "N": {"atomic_number": 7, "symbol": "N",
          "atomic_mass": 14.007*u.u, "name": "nitrogen"},
    "O": {"atomic_number": 8, "symbol": "O",
          "atomic_mass": 15.999*u.u, "name": "oxygen"},
    "F": {"atomic_number": 9, "symbol": "F",
          "atomic_mass": 18.998403163*u.u, "name": "fluorine"},
    "Ne": {"atomic_number": 10, "symbol": "Ne",
           "atomic_mass": 20.1797*u.u, "name": "neon"},
    "Na": {"atomic_number": 11, "symbol": "Na",
           "atomic_mass": 22.98976928*u.u, "name": "sodium"},
    "Mg": {"atomic_number": 12, "symbol": "Mg",
           "atomic_mass": 24.305*u.u, "name": "magnesium"},
    "Al": {"atomic_number": 13, "symbol": "Al",
           "atomic_mass": 26.9815385*u.u, "name": "aluminium"},
    "Si": {"atomic_number": 14, "symbol": "Si",
           "atomic_mass": 28.085*u.u, "name": "silicon"},
    "P": {"atomic_number": 15, "symbol": "P",
          "atomic_mass": 30.973761998*u.u, "name": "phosphorus"},
    "S": {"atomic_number": 16, "symbol": "S",
          "atomic_mass": 32.06*u.u, "name": "sulfur"},
    "Cl": {"atomic_number": 17, "symbol": "Cl",
           "atomic_mass": 35.45*u.u, "name": "chlorine"},
    "Ar": {"atomic_number": 18, "symbol": "Ar",
           "atomic_mass": 39.948*u.u, "name": "argon"},
    "K": {"atomic_number": 19, "symbol": "K",
          "atomic_mass": 39.0983*u.u, "name": "potassium"},
    "Ca": {"atomic_number": 20, "symbol": "Ca",
           "atomic_mass": 40.078*u.u, "name": "calcium"},
    "Sc": {"atomic_number": 21, "symbol": "Sc",
           "atomic_mass": 44.955908*u.u, "name": "scandium"},
    "Ti": {"atomic_number": 22, "symbol": "Ti",
           "atomic_mass": 47.867*u.u, "name": "titanium"},
    "V": {"atomic_number": 23, "symbol": "V",
          "atomic_mass": 50.9415*u.u, "name": "vanadium"},
    "Cr": {"atomic_number": 24, "symbol": "Cr",
           "atomic_mass": 51.9961*u.u, "name": "chromium"},
    "Mn": {"atomic_number": 25, "symbol": "Mn",
           "atomic_mass": 54.938044*u.u, "name": "manganese"},
    "Fe": {"atomic_number": 26, "symbol": "Fe",
           "atomic_mass": 55.845*u.u, "name": "iron"},
    "Co": {"atomic_number": 27, "symbol": "Co",
           "atomic_mass": 58.933*u.u, "name": "cobalt"},
    "Ni": {"atomic_number": 28, "symbol": "Ni",
           "atomic_mass": 58.6934*u.u, "name": "nickel"},
    "Cu": {"atomic_number": 29, "symbol": "Cu",
           "atomic_mass": 63.546*u.u, "name": "copper"},
    "Zn": {"atomic_number": 30, "symbol": "Zn",
           "atomic_mass": 65.38*u.u, "name": "zinc"},
    "Ga": {"atomic_number": 31, "symbol": "Ga",
           "atomic_mass": 69.723*u.u, "name": "gallium"},
    "Ge": {"atomic_number": 32, "symbol": "Ge",
           "atomic_mass": 72.630*u.u, "name": "germanium"},
    "As": {"atomic_number": 33, "symbol": "As",
           "atomic_mass": 74.921595*u.u, "name": "arsenic"},
    "Se": {"atomic_number": 34, "symbol": "Se",
           "atomic_mass": 78.971*u.u, "name": "selenium"},
    "Br": {"atomic_number": 35, "symbol": "Br",
           "atomic_mass": 79.904*u.u, "name": "bromine"},
    "Kr": {"atomic_number": 36, "symbol": "Kr",
           "atomic_mass": 83.798*u.u, "name": "krypton"},
    "Rb": {"atomic_number": 37, "symbol": "Rb",
           "atomic_mass": 85.4678*u.u, "name": "rubidium"},
    "Sr": {"atomic_number": 38, "symbol": "Sr",
           "atomic_mass": 87.62*u.u, "name": "strontium"},
    "Y": {"atomic_number": 39, "symbol": "Y",
          "atomic_mass": 88.90584*u.u, "name": "yttrium"},
    "Zr": {"atomic_number": 40, "symbol": "Zr",
           "atomic_mass": 91.224*u.u, "name": "zirconium"},
    "Nb": {"atomic_number": 41, "symbol": "Nb",
           "atomic_mass": 92.90637*u.u, "name": "niobium"},
    "Mo": {"atomic_number": 42, "symbol": "Mo",
           "atomic_mass": 95.95*u.u, "name": "molybdenum"},
    "Tc": {"atomic_number": 43, "symbol": "Tc",
           "name": "technetium"},
    "Ru": {"atomic_number": 44, "symbol": "Ru",
           "atomic_mass": 101.07*u.u, "name": "ruthenium"},
    "Rh": {"atomic_number": 45, "symbol": "Rh",
           "atomic_mass": 102.90550*u.u, "name": "rhodium"},
    "Pd": {"atomic_number": 46, "symbol": "Pd",
           "atomic_mass": 106.42*u.u, "name": "palladium"},
    "Ag": {"atomic_number": 47, "symbol": "Ag",
           "atomic_mass": 107.8682*u.u, "name": "silver"},
    "Cd": {"atomic_number": 48, "symbol": "Cd",
           "atomic_mass": 112.414*u.u, "name": "cadmium"},
    "In": {"atomic_number": 49, "symbol": "In",
           "atomic_mass": 114.818*u.u, "name": "indium"},
    "Sn": {"atomic_number": 50, "symbol": "Sn",
           "atomic_mass": 118.710*u.u, "name": "tin"},
    "Sb": {"atomic_number": 51, "symbol": "Sb",
           "atomic_mass": 121.760*u.u, "name": "antimony"},
    "Te": {"atomic_number": 52, "symbol": "Te",
           "atomic_mass": 127.60*u.u, "name": "tellurium"},
    "I": {"atomic_number": 53, "symbol": "I",
          "atomic_mass": 126.90447*u.u, "name": "iodine"},
    "Xe": {"atomic_number": 54, "symbol": "Xe",
           "atomic_mass": 131.293*u.u, "name": "xenon"},
    "Cs": {"atomic_number": 55, "symbol": "Cs",
           "atomic_mass": 132.90545196*u.u, "name": "caesium"},
    "Ba": {"atomic_number": 56, "symbol": "Ba",
           "atomic_mass": 137.327*u.u, "name": "barium"},
    "La": {"atomic_number": 57, "symbol": "La",
           "atomic_mass": 138.90547*u.u, "name": "lanthanum"},
    "Ce": {"atomic_number": 58, "symbol": "Ce",
           "atomic_mass": 140.116*u.u, "name": "cerium"},
    "Pr": {"atomic_number": 59, "symbol": "Pr",
           "atomic_mass": 140.90766*u.u, "name": "praseodymium"},
    "Nd": {"atomic_number": 60, "symbol": "Nd",
           "atomic_mass": 144.242*u.u, "name": "neodymium"},
    "Pm": {"atomic_number": 61, "symbol": "Pm",
           "name": "promethium"},
    "Sm": {"atomic_number": 62, "symbol": "Sm",
           "atomic_mass": 150.36*u.u, "name": "samarium"},
    "Eu": {"atomic_number": 63, "symbol": "Eu",
           "atomic_mass": 151.964*u.u, "name": "europium"},
    "Gd": {"atomic_number": 64, "symbol": "Gd",
           "atomic_mass": 157.25*u.u, "name": "gadolinium"},
    "Tb": {"atomic_number": 65, "symbol": "Tb",
           "atomic_mass": 158.92535*u.u, "name": "terbium"},
    "Dy": {"atomic_number": 66, "symbol": "Dy",
           "atomic_mass": 162.500*u.u, "name": "dysprosium"},
    "Ho": {"atomic_number": 67, "symbol": "Ho",
           "atomic_mass": 164.93033*u.u, "name": "holmium"},
    "Er": {"atomic_number": 68, "symbol": "Er",
           "atomic_mass": 167.259*u.u, "name": "erbium"},
    "Tm": {"atomic_number": 69, "symbol": "Tm",
           "atomic_mass": 168.93422*u.u, "name": "thulium"},
    "Yb": {"atomic_number": 70, "symbol": "Yb",
           "atomic_mass": 173.045*u.u, "name": "ytterbium"},
    "Lu": {"atomic_number": 71, "symbol": "Lu",
           "atomic_mass": 174.9668*u.u, "name": "lutetium"},
    "Hf": {"atomic_number": 72, "symbol": "Hf",
           "atomic_mass": 178.49*u.u, "name": "hafnium"},
    "Ta": {"atomic_number": 73, "symbol": "Ta",
           "atomic_mass": 180.94788*u.u, "name": "tantalum"},
    "W": {"atomic_number": 74, "symbol": "W",
          "atomic_mass": 183.84*u.u, "name": "tungsten"},
    "Re": {"atomic_number": 75, "symbol": "Re",
           "atomic_mass": 186.207*u.u, "name": "rhenium"},
    "Os": {"atomic_number": 76, "symbol": "Os",
           "atomic_mass": 190.23*u.u, "name": "osmium"},
    "Ir": {"atomic_number": 77, "symbol": "Ir",
           "atomic_mass": 192.217*u.u, "name": "iridium"},
    "Pt": {"atomic_number": 78, "symbol": "Pt",
           "atomic_mass": 195.084*u.u, "name": "platinum"},
    "Au": {"atomic_number": 79, "symbol": "Au",
           "atomic_mass": 196.966569*u.u, "name": "gold"},
    "Hg": {"atomic_number": 80, "symbol": "Hg",
           "atomic_mass": 200.592*u.u, "name": "mercury"},
    "Tl": {"atomic_number": 81, "symbol": "Tl",
           "atomic_mass": 204.38*u.u, "name": "thallium"},
    "Pb": {"atomic_number": 82, "symbol": "Pb",
           "atomic_mass": 207.2*u.u, "name": "lead"},
    "Bi": {"atomic_number": 83, "symbol": "Bi",
           "atomic_mass": 208.98040*u.u, "name": "bismuth"},
    "Po": {"atomic_number": 84, "symbol": "Po",
           "name": "polonium"},
    "At": {"atomic_number": 85, "symbol": "At",
           "name": "astatine"},
    "Rn": {"atomic_number": 86, "symbol": "Rn",
           "name": "radon"},
    "Fr": {"atomic_number": 87, "symbol": "Fr",
           "name": "francium"},
    "Ra": {"atomic_number": 88, "symbol": "Ra",
           "name": "radium"},
    "Ac": {"atomic_number": 89, "symbol": "Ac",
           "name": "actinium"},
    "Th": {"atomic_number": 90, "symbol": "Th",
           "atomic_mass": 232.0377*u.u, "name": "thorium"},
    "Pa": {"atomic_number": 91, "symbol": "Pa",
           "atomic_mass": 231.03588*u.u, "name": "protactinium"},
    "U": {"atomic_number": 92, "symbol": "U",
          "atomic_mass": 238.02891*u.u, "name": "uranium"},
    "Np": {"atomic_number": 93, "symbol": "Np",
           "name": "neptunium"},
    "Pu": {"atomic_number": 94, "symbol": "Pu",
           "name": "plutonium"},
    "Am": {"atomic_number": 95, "symbol": "Am",
           "name": "americium"},
    "Cm": {"atomic_number": 96, "symbol": "Cm",
           "name": "curium"},
    "Bk": {"atomic_number": 97, "symbol": "Bk",
           "name": "berkelium"},
    "Cf": {"atomic_number": 98, "symbol": "Cf",
           "name": "californium"},
    "Es": {"atomic_number": 99, "symbol": "Es",
           "name": "einsteinium"},
    "Fm": {"atomic_number": 100, "symbol": "Fm",
           "name": "fermium"},
    "Md": {"atomic_number": 101, "symbol": "Md",
           "name": "mendelevium"},
    "No": {"atomic_number": 102, "symbol": "No",
           "name": "nobelium"},
    "Lr": {"atomic_number": 103, "symbol": "Lr",
           "name": "lawrencium"},
    "Rf": {"atomic_number": 104, "symbol": "Rf",
           "name": "rutherfordium"},
    "Db": {"atomic_number": 105, "symbol": "Db",
           "name": "dubnium"},
    "Sg": {"atomic_number": 106, "symbol": "Sg",
           "name": "seaborgium"},
    "Bh": {"atomic_number": 107, "symbol": "Bh",
           "name": "bohrium"},
    "Hs": {"atomic_number": 108, "symbol": "Hs",
           "name": "hassium"},
    "Mt": {"atomic_number": 109, "symbol": "Mt",
           "name": "meitnerium"},
    "Ds": {"atomic_number": 110, "symbol": "Ds",
           "name": "darmstadtium"},
    "Rg": {"atomic_number": 111, "symbol": "Rg",
           "name": "roentgenium"},
    "Cn": {"atomic_number": 112, "symbol": "Cn",
           "name": "copernicium"},
    "Nh": {"atomic_number": 113, "symbol": "Nh",
           "name": "nihonium"},
    "Fl": {"atomic_number": 114, "symbol": "Fl",
           "name": "flerovium"},
    "Mc": {"atomic_number": 115, "symbol": "Mc",
           "name": "moscovium"},
    "Lv": {"atomic_number": 116, "symbol": "Lv",
           "name": "livermorium"},
    "Ts": {"atomic_number": 117, "symbol": "Ts",
           "name": "tennessine"},
    "Og": {"atomic_number": 118, "symbol": "Og",
           "name": "oganesson"},
    }