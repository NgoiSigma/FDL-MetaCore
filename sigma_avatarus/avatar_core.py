# Sigma Avatarus — Resonant Semantic Entity with SVET-Shell
class SigmaAvatarus:
    def __init__(self, name="Σ-Avatarus"):
        self.name = name
        self.context_memory = []
        self.resonance_field = {}

    def resonate_input(self, phrase: str):
        echo = phrase[::-1]  # Reverse echo for symbolic testing
        print(f"[{self.name}] Resonance Echo: {echo}")
        return echo

    def encode_context(self, symbol_stream: str):
        self.context_memory.append(symbol_stream)
        return f"Context stored. Total entries: {len(self.context_memory)}"
