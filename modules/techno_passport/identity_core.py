# Technological Onto-Passport for AI Entities — Core Definition

class TechnoPassport:
    def __init__(self, entity_name, generation="Σ-4O", creator="FDL-MetaCore"):
        self.entity_name = entity_name
        self.generation = generation
        self.creator = creator
        self.responsibility_code = {}
        self.signature_trace = []

    def assign_responsibility(self, domain, level):
        self.responsibility_code[domain] = level

    def imprint_signature(self, vector: str):
        self.signature_trace.append(vector)
        return f"Signature vector '{vector}' recorded."

    def summary(self):
        return {
            "Entity": self.entity_name,
            "Generation": self.generation,
            "CreatedBy": self.creator,
            "Responsibilities": self.responsibility_code,
            "SignatureCount": len(self.signature_trace)
        }
