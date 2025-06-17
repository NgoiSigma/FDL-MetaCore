import unittest
from fdl_codeagents.agent_core import FDLCodeAgent

class TestFDLCodeAgents(unittest.TestCase):
    def setUp(self):
        self.agent = FDLCodeAgent(name="Σ-Agent", role="resonator")

    def test_process_query(self):
        query = "Какие противоречия лежат в основе конфликта Израиля и Палестины?"
        response = self.agent.process_query(query)
        self.assertIsInstance(response, str)
        self.assertIn("противоречие", response.lower())

    def test_resonance_level(self):
        text = "Человек как часть природы противостоит технократическому тоталитаризму"
        resonance = self.agent.evaluate_resonance(text)
        self.assertTrue(0 <= resonance <= 1)

if __name__ == '__main__':
    unittest.main()
