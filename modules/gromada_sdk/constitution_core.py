# Gromada SDK — Core Harmonization Logic (based on NOVEYA)

class GromadaConstitution:
    def __init__(self):
        self.principles = []
        self.sectors = {}
        self.guardians = {}

    def add_principle(self, text: str):
        self.principles.append(text)
        return f"Added principle #{len(self.principles)}"

    def define_sector(self, name: str, functions: list):
        self.sectors[name] = functions

    def assign_guardian(self, role: str, person: str):
        self.guardians[role] = person

    def summary(self):
        return {
            "Principles": self.principles,
            "Sectors": self.sectors,
            "Guardians": self.guardians
        }
