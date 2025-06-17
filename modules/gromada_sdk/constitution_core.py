# modules/gromada_sdk/constitution_core.py

import json
import os

class GromadaConstitution:
    def __init__(self):
        self.core_values = {
            "Wisdom": None,
            "Peacekeeper": None,
            "Seed Keeper": None
        }

    def assign_guardian(self, role, name):
        if role in self.core_values:
            self.core_values[role] = name
            print(f"[✓] Guardian '{name}' assigned to role '{role}'")
        else:
            print(f"[!] Unknown role: {role}")

    def summary(self):
        return self.core_values

    def load_guardians_from_file(self, path="guardians.json"):
        try:
            full_path = os.path.join(os.path.dirname(__file__), path)
            with open(full_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for role, name in data.items():
                    self.assign_guardian(role, name)
            print("[✓] Guardians loaded successfully.")
        except Exception as e:
            print(f"[!] Failed to load guardians: {e}")
