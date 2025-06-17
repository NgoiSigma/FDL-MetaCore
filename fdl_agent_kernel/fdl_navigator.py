# FDL Logical Navigator — Synthesizes Contradictions and Guides Agent Reasoning
class FDLNavigator:
    def __init__(self):
        self.dialectical_log = []

    def navigate(self, thesis: str, antithesis: str):
        synthesis = f"SYN[{thesis}] ↔ [{antithesis}]"
        self.dialectical_log.append((thesis, antithesis, synthesis))
        return synthesis

    def memory_log(self):
        return self.dialectical_log[-5:]
