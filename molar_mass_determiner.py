#  Jacob Meadows
#  Computer Programming, 4th Period
#  December 6th, 2017


class MolarMass:
    def __init__(self):
        self.masses = {
            "H": ["Hydrogen", 1.0079],
            "He": ["Helium", 4.0026],
            "Li": ["Lithium", 6.941],
            "Be": ["Beryllium", 9.0122],
            "B": ["Boron", 10.811],
            "C": ["Carbon", 12.011],
            "N": ["Nitrogen", 14.0067],
            "O": ["Oxygen", 15.9994],
            "F": ["Fluorine", 18.9984],
            "Ne": ["Neon", 20.1797],
            "Na": ["Sodium", 22.9898],
            "Mg": ["Magnesium", 24.3050]
        }
        self.molecule_name = input("Molecule or Ion: ")
        self.name = self.molecule_name
        self.mass = self.masses[self.name]


MolarMass()